import pandas as pd
import numpy as np
import os

class MomentumEngine:
    def __init__(self):
        # 2026 Ground Truth: Rest Day Matrix
        # Sunday Winners (4 days rest): High Fatigue
        self.sunday_tids = [1116, 1345, 1412, 1433, 1301] # Ark, Purd, UAB, VCU, NC St
        # Saturday/Friday Winners (5-6 days rest): Optimal Rest
        self.optimal_rest_tids = [1181, 1163, 1112, 1222, 1211, 3163, 3437] # Duke, UConn, AZ, Hou, Gonz
        # Conference Champions (Momentum Boost)
        self.champs = [1116, 1345, 1112, 1181, 1385, 1211, 3163, 3437, 3261] 

    def apply_momentum_rest(self, sub_path):
        print("Applying 2026 Rest and Momentum taxes...")
        df = pd.read_csv(sub_path)

        def calculate_fatigue(row):
            parts = row['ID'].split('_')
            t1, t2 = int(parts[1]), int(parts[2])
            prob = row['Pred']

            # 1. The Sunday Tax (-4% penalty for short rest)
            if t1 in self.sunday_tids: prob -= 0.04
            if t2 in self.sunday_tids: prob += 0.04

            # 2. Championship Momentum (+2.5% boost)
            if t1 in self.champs: prob += 0.025
            if t2 in self.champs: prob -= 0.025

            # 3. Optimal Rest Window (+1.5% boost)
            if t1 in self.optimal_rest_tids: prob += 0.015
            if t2 in self.optimal_rest_tids: prob -= 0.015

            return np.clip(prob, 0.01, 0.99)

        df['Pred'] = df.apply(calculate_fatigue, axis=1)
        os.makedirs("submissions", exist_ok=True)
        out_name = os.path.join("submissions", "submission_2026_momentum.csv")
        df.to_csv(out_name, index=False)
        print(f"Success: Momentum and Fatigue applied. Saved to {out_name}")

if __name__ == "__main__":
    MomentumEngine().apply_momentum_rest(os.path.join("submissions", "submission_2026_geospatial.csv"))
