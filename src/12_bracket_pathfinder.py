import pandas as pd
import numpy as np
import os

class BracketPathfinder:
    def __init__(self, gender='M'):
        self.gender = gender
        self.prob_path = f"data/processed/{self.gender}_bracket_probabilities_2026.csv"

    def find_value_upsets(self, threshold=0.15):
        """Identifies double-digit seeds with high advancement potential."""
        df = pd.read_csv(self.prob_path)
        
        # Robust Seed extraction and filtering
        df['SeedNum'] = df['Seed'].str.extract('(\d+)').astype(float).fillna(0).astype(int)
        
        # Filter for seeds 10-16 that have a high S16 probability
        # Lowered threshold to 15% as 35% is nearly impossible for a 12-seed
        upsets = df[(df['SeedNum'] >= 10) & (df['S16'] > threshold)].copy()
        
        print(f"\n--- 2026 {self.gender} VALUE UPSET WATCH (S16 Prob > {threshold*100}%) ---")
        if upsets.empty:
            print(f"No high-confidence deep upsets (>{threshold*100}%) detected.")
        else:
            # Highlight the 'Cinderella Score' (S16 prob * Seed)
            upsets['Cinderella_Score'] = upsets['S16'] * upsets['SeedNum']
            cols = ['TeamName', 'Seed', 'R32', 'S16']
            print(upsets[cols].sort_values('S16', ascending=False))

    def generate_optimal_path(self):
        df = pd.read_csv(self.prob_path)
        top = df.iloc[0]
        print(f"\n--- OPTIMAL PATH FOR: {top['TeamName']} ({top['Seed']}) ---")
        print(f"  R32: {top['R32']:.2%} | S16: {top['S16']:.2%} | F4: {top['F4']:.2%} | Champ: {top['Champ']:.2%}")

if __name__ == "__main__":
    for g in ['M', 'W']:
        path = BracketPathfinder(g)
        path.find_value_upsets(threshold=0.10) # 10% is the 'Gold Standard' for a 12/13 seed
        path.generate_optimal_path()