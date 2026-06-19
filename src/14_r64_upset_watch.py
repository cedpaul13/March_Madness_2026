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

class UpsetWatch:
    def __init__(self, gender='M'):
        self.gender = gender
        self.raw_path = "data/raw"
        self.fused_path = os.path.join("submissions", "submission_2026_CFA_FUSION.csv")
        self.loader = DataLoader(self.gender)
        self.preds = pd.read_csv(self.fused_path).set_index('ID')
        
        seeds_file = f"2026_{self.gender}Seeds.csv"
        self.seeds_df = pd.read_csv(os.path.join(self.raw_path, seeds_file))
        self.seeds_df['TeamID'] = self.seeds_df['TeamName'].apply(self.loader._basic_clean).map(self.loader.id_map)
        
        self.team_names = self.seeds_df.set_index('TeamID')['TeamName'].to_dict()
        self.team_seeds = self.seeds_df.set_index('TeamID')['Seed'].to_dict()
        
        all_slots = pd.read_csv(os.path.join(self.raw_path, f"{self.gender}NCAATourneySlots.csv"))
        self.slots = all_slots[all_slots['Season'] == 2026]

        # CORRECTED 2026 M MATCHUPS
        # Y11 = Miami OH vs (6) Tennessee 
        # Z08/Z09 = Clemson vs Iowa
        # Y08/Y09 = Georgia vs Saint Louis
        self.winners = {
            'M': {'Y16': 'Howard', 'X11': 'Texas', 'Z16': 'Prairie View', 'Y11': 'Miami OH'},
            'W': {'Y16': 'Missouri St'}
        }.get(self.gender, {})

    def fmt_s(self, tid):
        raw_seed = self.team_seeds.get(tid, "??")
        num = re.search(r'\d+', raw_seed)
        return f"({int(num.group())})" if num else "(??)"

    def get_prob(self, t1, t2):
        id_str = f"2026_{min(t1, t2)}_{max(t1, t2)}"
        try:
            p = self.preds.loc[id_str, 'Pred']
            return p if t1 < t2 else 1 - p
        except: return 0.5

    def run(self, threshold=0.70):
        print(f"\n{'='*20} 2026 {self.gender} R64 UPSET WATCH {'='*20}")
        print(f"{'MATCHUP':<45} | {'FAV PROB':<10} | {'STATUS'}")
        print("-" * 80)
        
        # Build map with actual play-in results
        seed_map = {row['Seed']: row['TeamID'] for _, row in self.seeds_df.iterrows() if not pd.isna(row['TeamID'])}
        for slot, name in self.winners.items():
            tid = self.loader.id_map.get(self.loader._basic_clean(name))
            if tid: seed_map[slot] = tid

        r1 = self.slots[self.slots['Slot'].str.startswith('R1')]
        for _, row in r1.iterrows():
            t1, t2 = seed_map.get(row['StrongSeed']), seed_map.get(row['WeakSeed'])
            if t1 and t2:
                p1 = self.get_prob(t1, t2)
                fav_prob = max(p1, 1-p1)
                
                if fav_prob < threshold:
                    f_idx = t1 if p1 > 0.5 else t2
                    u_idx = t2 if p1 > 0.5 else t1
                    matchup_str = f"{self.team_names[f_idx]} {self.fmt_s(f_idx)} vs {self.team_names[u_idx]} {self.fmt_s(u_idx)}"
                    print(f"{matchup_str:<45} | {fav_prob:>8.2%} | !!!! ALERT !!!!")

if __name__ == "__main__":
    for g in ['M', 'W']:
        UpsetWatch(g).run()
