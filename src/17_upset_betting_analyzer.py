import pandas as pd
import numpy as np
from scipy.stats import norm

class UpsetBettingAnalyzer:
    def __init__(self, gender='M'):
        self.gender = gender
        self.feat_path = f"data/processed/{self.gender}_full_features_2026.csv"
        self.sub_path = "submission_2026_CFA_FUSION.csv"
        
        # Target Matchups for Analysis
        self.targets = {
            'M': [
                (1208, 1234, "Georgia", "Iowa"),
                (1437, 1429, "Villanova", "Utah St"),
                (1155, 1387, "Clemson", "St Louis")
            ],
            'W': [
                (3235, 3393, "Iowa St", "Syracuse"),
                (3332, 3439, "Oregon", "Virginia Tech"),
                (3425, 3155, "USC", "Clemson")
            ]
        }.get(gender, [])

    def get_odds(self, t1_id, t2_id, t1_name, t2_name):
        feats = pd.read_csv(self.feat_path).set_index('TeamID')
        subs = pd.read_csv(self.sub_path).set_index('ID')
        
        # 1. Projected Score & Total (Efficiency * Pace)
        pace = (feats.loc[t1_id, 'adjt'] + feats.loc[t2_id, 'adjt']) / 2
        score1 = (feats.loc[t1_id, 'adjoe'] + feats.loc[t2_id, 'adjde'])/2 * (pace/100)
        score2 = (feats.loc[t2_id, 'adjoe'] + feats.loc[t1_id, 'adjde'])/2 * (pace/100)
        
        # 2. Moneyline (Win Prob -> American Odds)
        id_str = f"2026_{min(t1_id, t2_id)}_{max(t1_id, t2_id)}"
        p = subs.loc[id_str, 'Pred']
        p_fav = p if t1_id < t2_id else 1 - p
        
        def to_ml(prob):
            if prob >= 0.5: return int(-100 * prob / (1 - prob))
            return int(100 * (1 - prob) / prob)

        # 3. Spread (Using 11.0 Standard Deviation for neutral sites)
        spread = round(norm.ppf(p_fav) * 11.0 * 2) / 2
        
        return {
            "matchup": f"{t1_name} vs {t2_name}",
            "proj_score": f"{int(score1)}-{int(score2)}",
            "total": round(score1 + score2, 1),
            "ml": (to_ml(p_fav), to_ml(1-p_fav)),
            "spread": -abs(spread)
        }

    def run_report(self):
        print(f"\n{'='*20} 2026 {self.gender} UPSET BETTING BOARD {'='*20}")
        print(f"{'MATCHUP':<30} | {'PROJ':<8} | {'TOTAL':<6} | {'ML (F/U)':<15} | {'SPREAD'}")
        print("-" * 75)
        
        for t1_id, t2_id, n1, n2 in self.targets:
            o = self.get_odds(t1_id, t2_id, n1, n2)
            print(f"{o['matchup']:<30} | {o['proj_score']:<8} | {o['total']:<6} | {o['ml'][0]:>6}/{o['ml'][1]:<7} | {o['spread']:>6}")

if __name__ == "__main__":
    for g in ['M', 'W']:
        UpsetBettingAnalyzer(g).run_report()