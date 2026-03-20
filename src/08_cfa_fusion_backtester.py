import pandas as pd
import numpy as np
import os

class CFAEnsembler:
    def __init__(self):
        self.proc_path = "data/processed"
        # Weights derived from "Diversity Strength" (CFA Paper logic)
        self.weights = {
            'stats': 0.50,    # Base efficiency (XGBoost)
            'geo': 0.25,      # Travel burden
            'momentum': 0.25  # Rest & Injury
        }

    def fuse_rank_score(self, m_path, g_path):
        """
        Implements Combinatorial Fusion Analysis.
        Fuses raw probabilities with their ordinal ranks.
        """
        print(f"Applying CFA Fusion to {m_path}...")
        
        # 1. Load component models
        df_raw = pd.read_csv("submission_2026_raw.csv") # Agent 1: Stats
        df_geo = pd.read_csv("submission_2026_geospatial.csv") # Agent 2: Geo
        df_mom = pd.read_csv("submission_2026_momentum.csv") # Agent 3: Momentum

        # 2. Score Combination (CFA Score)
        # $S_{cfa} = \sum (w_i \cdot P_i)$
        score_fusion = (df_raw['Pred'] * self.weights['stats'] + 
                        df_geo['Pred'] * self.weights['geo'] + 
                        df_mom['Pred'] * self.weights['momentum'])

        # 3. Rank Combination (CFA Rank)
        # We convert probabilities to ranks (1 = strongest favorite)
        # This stabilizes the Caleb Foster/Injury variance
        r1 = df_raw['Pred'].rank(ascending=False)
        r2 = df_geo['Pred'].rank(ascending=False)
        r3 = df_mom['Pred'].rank(ascending=False)
        
        rank_fusion = (r1 * self.weights['stats'] + 
                       r2 * self.weights['geo'] + 
                       r3 * self.weights['momentum']).rank(ascending=True)
        
        # 4. Final Meta-Fusion
        # Normalize rank fusion back to 0-1 probability space
        rank_prob = 1 - (rank_fusion / len(df_raw))
        
        # Final blend: 70% Score / 30% Rank (Paper's suggested ratio for accuracy)
        final_pred = (score_fusion * 0.7) + (rank_prob * 0.3)
        
        df_raw['Pred'] = np.clip(final_pred, 0.015, 0.985)
        
        out_path = "submission_2026_CFA_FUSION.csv"
        df_raw[['ID', 'Pred']].to_csv(out_path, index=False)
        print(f"CFA Fusion Complete. Final Kaggle Submission: {out_path}")

if __name__ == "__main__":
    CFAEnsembler().fuse_rank_score("submission_2026_raw.csv", "submission_2026_geospatial.csv")