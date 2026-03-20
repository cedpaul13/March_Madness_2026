import pandas as pd
import numpy as np
import os
import re
import importlib.util

def get_loader():
    spec = importlib.util.spec_from_file_location("data_loader_01", "src/01_data_loader.py")
    dl_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dl_mod)
    return dl_mod.DataLoader

DataLoader = get_loader()

class BracketArchitect:
    def __init__(self, gender='M'):
        self.gender = gender
        self.raw_path = "data/raw"
        self.fused_path = "submission_2026_CFA_FUSION.csv"
        self.loader = DataLoader(self.gender)
        self.preds = pd.read_csv(self.fused_path).set_index('ID')
        
        # Quadrant Order & Naming - Synced for 2026 Rotation
        if self.gender == 'M':
            self.quad_config = [
                ('W', 'EAST'), ('Z', 'SOUTH'), ('X', 'WEST'), ('Y', 'MID-WEST')
            ]
        else:
            self.quad_config = [
                ('W', 'FORT WORTH 1'), ('Z', 'SACRAMENTO 4'), 
                ('Y', 'SACRAMENTO 2'), ('X', 'FORT WORTH 3')
            ]

        # Pairing Order (1v16, 8v9, 5v12, 4v13, 6v11, 3v14, 7v10, 2v15)
        self.r1_order = [1, 8, 5, 4, 6, 3, 7, 2]

        all_slots = pd.read_csv(os.path.join(self.raw_path, f"{self.gender}NCAATourneySlots.csv"))
        self.slots_df = all_slots[all_slots['Season'] == 2026]
        
        seeds_file = f"2026_{self.gender}Seeds.csv"
        self.seeds_2026 = pd.read_csv(os.path.join(self.raw_path, seeds_file))
        self.seeds_2026['TeamID'] = self.seeds_2026['TeamName'].apply(self.loader._basic_clean).map(self.loader.id_map)
        
        self.team_names = self.seeds_2026.set_index('TeamID')['TeamName'].to_dict()
        self.team_seeds = self.seeds_2026.set_index('TeamID')['Seed'].to_dict()
        
        # Suffix-safe seed mapping
        self.seed_map = {}
        counts = {}
        for _, row in self.seeds_2026.iterrows():
            s, tid = row['Seed'], row['TeamID']
            if pd.isna(tid): continue
            if s not in counts:
                counts[s] = 1
                self.seed_map[s] = int(tid)
            else:
                orig_id = self.seed_map.pop(s)
                self.seed_map[f"{s}a"] = int(orig_id)
                self.seed_map[f"{s}b"] = int(tid)
                counts[s] += 1

    def fmt_s(self, tid):
        raw_seed = self.team_seeds.get(tid, "??")
        num = re.search(r'\d+', raw_seed)
        return f"({int(num.group())})" if num else "(??)"

    def get_winner(self, t1, t2):
        if t1 == t2: return t1
        id_str = f"2026_{min(t1, t2)}_{max(t1, t2)}"
        try:
            p = self.preds.loc[id_str, 'Pred']
            p1 = p if t1 < t2 else 1 - p
            return t1 if p1 >= 0.50 else t2
        except: return t1

    def build_bracket(self):
        print(f"\n{'='*25} 2026 {self.gender} MASTER ARCHITECT {'='*25}")
        state = self.seed_map.copy()

        # 1. Resolve Play-Ins (Verified 2026 Ground Truths)
        play_ins = self.slots_df[~self.slots_df['Slot'].str.startswith('R')]
        for _, row in play_ins.iterrows():
            slot = row['Slot']
            if slot == 'Y16' and self.gender == 'M': winner_id = 1224 # Howard
            elif slot == 'X11' and self.gender == 'M': winner_id = 1251 # Texas
            elif slot == 'Z16' and self.gender == 'M': winner_id = 1341 # Prairie View
            else:
                t1, t2 = state.get(row['StrongSeed']), state.get(row['WeakSeed'])
                winner_id = self.get_winner(t1, t2) if (t1 and t2) else (t1 or t2)
            state[slot] = winner_id

        # 2. Quadrant Resolution (R1-R4)
        for r_code, r_name in self.quad_config:
            print(f"\n>>> QUADRANT: {r_name} <<<")
            
            print("\n  [ROUND OF 64]")
            for slot_num in self.r1_order:
                slot_id = f"R1{r_code}{slot_num}"
                rows = self.slots_df[self.slots_df['Slot'] == slot_id]
                if rows.empty: continue
                row = rows.iloc[0]
                t1, t2 = state.get(row['StrongSeed']), state.get(row['WeakSeed'])
                if t1 and t2:
                    w = self.get_winner(t1, t2)
                    state[slot_id] = w
                    print(f"    {slot_id}: {self.team_names[t1]} {self.fmt_s(t1)} vs {self.team_names[t2]} {self.fmt_s(t2)} -> {self.team_names[w]} {self.fmt_s(w)}")
                elif t1:
                    state[slot_id] = t1
                    print(f"    {slot_id}: {self.team_names[t1]} {self.fmt_s(t1)} advances (BYE/FIRST FOUR)")

            for r, r_title in {2: "ROUND OF 32", 3: "SWEET 16", 4: "ELITE 8"}.items():
                print(f"\n  [{r_title}]")
                r_slots = self.slots_df[self.slots_df['Slot'].str.startswith(f"R{r}{r_code}")]
                for _, row in r_slots.iterrows():
                    t1, t2 = state.get(row['StrongSeed']), state.get(row['WeakSeed'])
                    if t1 and t2:
                        w = self.get_winner(t1, t2)
                        state[row['Slot']] = w
                        print(f"    {row['Slot']}: {self.team_names[t1]} {self.fmt_s(t1)} vs {self.team_names[t2]} {self.fmt_s(t2)} -> {self.team_names[w]} {self.fmt_s(w)}")

        # 3. Final Four and Championship (Cross-Regional Pairing Fix)
        print("\n" + "="*20 + " THE FINAL STRETCH " + "="*20)
        
        print("\n[FINAL FOUR]")
        # 2026 Pairings: W vs Z (East/FW1 vs South/SAC4) and Y vs X (Mid-West/SAC2 vs West/FW3)
        ff_pairings = [
            ('R5WX', f'R4W1', f'R4Z1'), 
            ('R5YZ', f'R4Y1', f'R4X1')
        ]
        
        for slot, strong, weak in ff_pairings:
            t1, t2 = state.get(strong), state.get(weak)
            if t1 and t2:
                w = self.get_winner(t1, t2)
                state[slot] = w
                print(f"  {slot}: {self.team_names[t1]} {self.fmt_s(t1)} vs {self.team_names[t2]} {self.fmt_s(t2)} -> {self.team_names[w]} {self.fmt_s(w)}")

        print("\n[NATIONAL CHAMPIONSHIP]")
        # R6CH: Winner of R5WX vs Winner of R5YZ
        t1, t2 = state.get('R5WX'), state.get('R5YZ')
        if t1 and t2:
            w = self.get_winner(t1, t2)
            print(f"  R6CH: {self.team_names[t1]} {self.fmt_s(t1)} vs {self.team_names[t2]} {self.fmt_s(t2)} -> {self.team_names[w]} {self.fmt_s(w)}")

if __name__ == "__main__":
    for g in ['M', 'W']:
        BracketArchitect(g).build_bracket()