import pandas as pd
import numpy as np
from scipy.stats import norm
import os

class ChampionshipBettingBoard:
    def __init__(self, gender='M'):
        self.gender = gender
        self.feat_path = f"data/processed/{self.gender}_full_features_2026.csv"
        self.sub_path = os.path.join("submissions", "submission_2026_CFA_FUSION.csv")
        
        # 2026 Championship Matchups from Architect
        self.matchup = {
            'M': (1181, 1276, "Duke", "Michigan"), # Duke (W1) vs Michigan (Y1)
            'W': (3163, 3376, "Connecticut", "South Carolina") # UConn (W1) vs SC (Z1)
        }.get(gender)

    def get_betting_metrics(self):
        t1_id, t2_id, t1_name, t2_name = self.matchup
        feats = pd.read_csv(self.feat_path).set_index('TeamID')
        subs = pd.read_csv(self.sub_path).set_index('ID')
        
        # 1. Score Projection (Efficiency * Pace)
        pace = (feats.loc[t1_id, 'adjt'] + feats.loc[t2_id, 'adjt']) / 2
        score1 = (feats.loc[t1_id, 'adjoe'] + feats.loc[t2_id, 'adjde'])/2 * (pace/100)
        score2 = (feats.loc[t2_id, 'adjoe'] + feats.loc[t1_id, 'adjde'])/2 * (pace/100)
        
        # 2. Moneyline Calculation (from Fusion Prob)
        id_str = f"2026_{min(t1_id, t2_id)}_{max(t1_id, t2_id)}"
        p = subs.loc[id_str, 'Pred']
        p1 = p if t1_id < t2_id else 1 - p
        
        def prob_to_ml(prob):
            if prob >= 0.5: return int(-100 * prob / (1 - prob))
            return int(100 * (1 - prob) / prob)

        # 3. Spread Calculation (Sigma=11 for neutral site)
        spread = round(norm.ppf(p1) * 11 * 2) / 2
        
        return {
            "teams": (t1_name, t2_name),
            "scores": (int(score1), int(score2)),
            "ml": (prob_to_ml(p1), prob_to_ml(1-p1)),
            "spread": -abs(spread),
            "total": round(score1 + score2, 1)
        }

    def display(self):
        m = self.get_betting_metrics()
        label = "MEN'S NATIONAL CHAMPIONSHIP" if self.gender == 'M' else "WOMEN'S NATIONAL CHAMPIONSHIP"
        date = "APRIL 6, 2026" if self.gender == 'M' else "APRIL 5, 2026"
        
        print(f"\n{'='*20} {label} {'='*20}")
        print(f"{' '*22} LUCAS OIL STADIUM | {date}")
        print("-" * 65)
        print(f"{'TEAM':<20} | {'SCORE':<8} | {'VEGAS ML':<10} | {'SPREAD'}")
        print("-" * 65)
        print(f"{m['teams'][0]:<20} | {m['scores'][0]:<8} | {m['ml'][0]:>8} | {m['spread']:>6}")
        print(f"{m['teams'][1]:<20} | {m['scores'][1]:<8} | {m['ml'][1]:>8} | {'+'+str(abs(m['spread'])):>6}")
        print("-" * 65)
        print(f"TOTAL (O/U): {m['total']}")
        print(f"PREDICTED WINNER: {m['teams'][0] if m['scores'][0] > m['scores'][1] else m['teams'][1]}")

if __name__ == "__main__":
    for g in ['M', 'W']:
        ChampionshipBettingBoard(g).display()
