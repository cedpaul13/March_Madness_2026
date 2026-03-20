import pandas as pd
import numpy as np
import os

class KagglePredictor:
    def __init__(self):
        self.raw_path = "data/raw"
        self.proc_path = "data/processed"
        self.template_path = os.path.join(self.raw_path, "SampleSubmissionStage2.csv")

    def generate_kaggle_file(self):
        print("Loading official Kaggle Template...")
        if not os.path.exists(self.template_path):
            print(f"Error: {self.template_path} not found. Please ensure SampleSubmissionStage2.csv is in data/raw/")
            return

        sub = pd.read_csv(self.template_path)
        
        # Load Engineered Full Field Features
        m_feats = pd.read_csv(f"{self.proc_path}/M_full_features_2026.csv").set_index('TeamID')
        w_feats = pd.read_csv(f"{self.proc_path}/W_full_features_2026.csv").set_index('TeamID')
        
        # Parse IDs: format 2026_T1_T2
        ids = sub['ID'].str.split('_', expand=True)
        sub['T1'] = ids[1].astype(int)
        sub['T2'] = ids[2].astype(int)
        
        def calculate_prob(row):
            t1, t2 = row['T1'], row['T2']
            # Determine Gender based on TeamID (Men: 1xxx, Women: 3xxx)
            feats = m_feats if t1 < 2000 else w_feats
            
            if t1 in feats.index and t2 in feats.index:
                f1 = feats.loc[t1]
                f2 = feats.loc[t2]
                
                # HEAD-TO-HEAD SIGMOID LOGIC
                # Delta Barthag (Efficiency) + Delta SeedNum (Relative strength)
                # Weights calibrated for Stage 2 Log-Loss Optimization
                raw_score = (f1['barthag'] - f2['barthag']) * 12.5 + (f1['SeedNum'] - f2['SeedNum']) * -0.55
                prob = 1 / (1 + np.exp(-raw_score))
                return np.clip(prob, 0.02, 0.98) # Prevent extreme log-loss penalties
            
            return 0.5 # Default fallback for teams not in current season stats

        print(f"Populating {len(sub)} matchups...")
        sub['Pred'] = sub.apply(calculate_prob, axis=1)
        
        out_path = "submission_2026_raw.csv"
        sub[['ID', 'Pred']].to_csv(out_path, index=False)
        print(f"Success! Created {out_path} with {len(sub)} rows.")

if __name__ == "__main__":
    KagglePredictor().generate_kaggle_file()