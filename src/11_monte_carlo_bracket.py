import pandas as pd
import numpy as np
import os
import importlib.util

def get_loader():
    spec = importlib.util.spec_from_file_location("data_loader_01", "src/01_data_loader.py")
    dl_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dl_mod)
    return dl_mod.DataLoader

DataLoader = get_loader()

class BracketSimulator:
    def __init__(self, gender='M', sims=10000):
        self.gender = gender
        self.num_sims = sims
        self.raw_path = "data/raw"
        self.sub_path = "submission_2026_CFA_FUSION.csv"
        
        self.preds = pd.read_csv(self.sub_path).set_index('ID')
        all_slots = pd.read_csv(os.path.join(self.raw_path, f"{self.gender}NCAATourneySlots.csv"))
        self.slots_2026 = all_slots[all_slots['Season'] == 2026].copy()
        
        loader = DataLoader(self.gender)
        self.seeds = loader.load_seeds()
        self.seed_map = self.seeds.groupby('Seed')['TeamID'].apply(list).to_dict()

    def get_prob(self, t1, t2):
        id_str = f"2026_{min(t1, t2)}_{max(t1, t2)}"
        try:
            p = self.preds.loc[id_str, 'Pred']
            return p if t1 < t2 else 1 - p
        except: return 0.5

    def simulate_tournament(self):
        print(f"Executing {self.num_sims} simulations for {self.gender}...")
        results = {tid: np.zeros(6) for tid in self.seeds['TeamID']}
        
        for _ in range(self.num_sims):
            state = {}
            for _, row in self.slots_2026.iterrows():
                slot, s_seed, w_seed = row['Slot'], row['StrongSeed'], row['WeakSeed']
                def resolve(s):
                    if s in state: return state[s]
                    base = s[:-1] if s[-1] in ['a', 'b'] else s
                    if base in self.seed_map:
                        idx = 1 if s.endswith('b') else 0
                        if idx < len(self.seed_map[base]): return self.seed_map[base][idx]
                    return None

                if not slot.startswith('R'):
                    t1, t2 = resolve(s_seed), resolve(w_seed)
                    if t1 and t2: state[slot] = t1 if np.random.random() < self.get_prob(t1, t2) else t2
                    elif t1: state[slot] = t1

            for r in range(1, 7):
                r_slots = self.slots_2026[self.slots_2026['Slot'].str.startswith(f"R{r}")]
                for _, row in r_slots.iterrows():
                    def get_id(s):
                        if s in state: return state[s]
                        if s in self.seed_map: return self.seed_map[s][0]
                        return None
                    t1, t2 = get_id(row['StrongSeed']), get_id(row['WeakSeed'])
                    if t1 and t2:
                        winner = t1 if np.random.random() < self.get_prob(t1, t2) else t2
                        state[row['Slot']] = winner
                        results[winner][r-1] += 1
        return self.format_results(results)

    def format_results(self, results):
        cols = ['R32', 'S16', 'E8', 'F4', 'Finals', 'Champ']
        df = pd.DataFrame.from_dict(results, orient='index', columns=cols) / self.num_sims
        # Crucial Fix: Ensure TeamID is a column, not just an index
        df.index.name = 'TeamID'
        df = df.reset_index()
        meta = self.seeds.groupby('TeamID').first()[['TeamName', 'Seed']].reset_index()
        return df.merge(meta, on='TeamID').sort_values('Champ', ascending=False)

if __name__ == "__main__":
    for g in ['M', 'W']:
        summary = BracketSimulator(g).simulate_tournament()
        summary.to_csv(f"data/processed/{g}_bracket_probabilities_2026.csv", index=False)