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

class EVCalculator:
    def __init__(self, gender='M'):
        self.gender = gender
        self.raw_path = "data/raw"
        self.sub_path = os.path.join("submissions", "submission_2026_CFA_FUSION.csv")
        self.loader = DataLoader(self.gender)
        
        # Load and map seeds
        seeds_file = f"2026_{self.gender}Seeds.csv"
        seeds_df = pd.read_csv(os.path.join(self.raw_path, seeds_file))
        
        self.seed_map = {}
        for _, row in seeds_df.iterrows():
            clean_name = self.loader._basic_clean(row['TeamName'])
            self.seed_map[clean_name] = row['Seed']

        self.high_risk_games = {
            'M': [(1208, 1234, "Georgia", "Iowa"), (1437, 1429, "Villanova", "Utah St")],
            'W': [(3235, 3393, "Iowa St", "Syracuse"), (3332, 3439, "Oregon", "Virginia Tech"), (3425, 3155, "USC", "Clemson")]
        }.get(self.gender, [])

    def fmt_seed(self, seed_str):
        """Strips region prefix and leading zeros (e.g., X08 -> 8)."""
        match = re.search(r'\d+', seed_str)
        return str(int(match.group())) if match else "??"

    def calculate_ev(self, model_p, vegas_ml):
        profit = vegas_ml if vegas_ml > 0 else (100 / abs(vegas_ml)) * 100
        return (model_p * profit) - ((1 - model_p) * 100)

    def run_leverage_report(self):
        header = f"=============== 2026 {self.gender} VALUE BETTING & LEVERAGE ==============="
        print(f"\n{header}")
        print(f"{'MATCHUP':<40} | {'MODEL %':<8} | {'VEGAS ML':<8} | {'EV ($100)'}")
        print("-" * 80)
        
        sub = pd.read_csv(self.sub_path)
        
        for t1, t2, n1, n2 in self.high_risk_games:
            id_str = f"2026_{min(t1, t2)}_{max(t1, t2)}"
            p = sub[sub['ID'] == id_str]['Pred'].values[0]
            model_p = p if t1 < t2 else 1 - p
            
            raw_s1 = self.seed_map.get(self.loader._basic_clean(n1), "??")
            raw_s2 = self.seed_map.get(self.loader._basic_clean(n2), "??")
            s1, s2 = self.fmt_seed(raw_s1), self.fmt_seed(raw_s2)
            
            matchup_str = f"{n1} ({s1}) vs {n2} ({s2})"
            vegas_ml = -110 
            ev = self.calculate_ev(model_p, vegas_ml)
            status = "SHARP" if ev > 5 else "AVOID"
            
            print(f"{matchup_str:<40} | {model_p:>7.2%} | {vegas_ml:>8} | ${ev:>8.2f} [{status}]")

if __name__ == "__main__":
    for g in ['M', 'W']:
        EVCalculator(g).run_leverage_report()
