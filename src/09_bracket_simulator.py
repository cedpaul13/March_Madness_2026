import pandas as pd
import numpy as np
import os

class BracketSimulator:
    def __init__(self, gender='M'):
        self.gender = gender
        self.sub_path = "submission_2026_CFA_FUSION.csv"
        self.raw_path = "data/raw"
        
    def get_matchup_prob(self, t1, t2):
        """Fetches the fused probability for a head-to-head."""
        sub = pd.read_csv(self.sub_path)
        id_str = f"2026_{min(t1, t2)}_{max(t1, t2)}"
        
        # Check if the matchup exists in our 132k grid
        row = sub[sub['ID'] == id_str]
        if not row.empty:
            p = row['Pred'].values[0]
            return p if t1 < t2 else 1 - p
        return 0.5

    def run_first_round_check(self):
        """Validates the 2026 'Red Flag' games."""
        print(f"\n--- 2026 {self.gender} Tactical Bracket Check ---")
        
        matchups = []
        if self.gender == 'M':
            # (6) UNC vs (11) VCU - The Caleb Wilson Fade
            matchups.append((1314, 1433, "6-UNC vs 11-VCU"))
            # (1) Duke vs (16) Siena - The Caleb Foster Test
            matchups.append((1181, 1373, "1-Duke vs 16-Siena"))
            # (4) Arkansas vs (13) Hawaii - The Calipari/Travel Factor
            matchups.append((1116, 1218, "4-Ark vs 13-Hawaii"))
        else:
            # (1) UConn vs (16) UTSA - The Auriemma Anchor
            matchups.append((3163, 3447, "1-UConn vs 16-UTSA"))
            
        for t1, t2, desc in matchups:
            p = self.get_matchup_prob(t1, t2)
            print(f"{desc}: Win Prob = {p:.2%}")

if __name__ == "__main__":
    for g in ['M', 'W']:
        sim = BracketSimulator(g)
        sim.run_first_round_check()