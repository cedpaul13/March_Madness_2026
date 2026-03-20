import pandas as pd
import numpy as np
from scipy.stats import norm
import os

class VegasSimulator:
    def __init__(self, gender='M'):
        self.gender = gender
        self.proc_path = "data/processed"
        self.sub_path = "submission_2026_CFA_FUSION.csv"
        # 2026 Ground Truth Thursday Schedule (EDT)
        self.schedule = {
            1181: "14:50", # Duke
            1116: "16:25", # Arkansas
            1314: "18:50", # UNC
            3163: "19:00"  # UConn (W) - Placeholder for session grouping
        }

    def prob_to_moneyline(self, p):
        if p >= 0.999: return "-10000"
        if p <= 0.001: return "+10000"
        if p > 0.5:
            ml = -100 * p / (1 - p)
            return f"{int(round(ml/10)*10)}"
        else:
            ml = (100 / p) - 100
            return f"+{int(round(ml/10)*10)}"

    def prob_to_spread(self, p):
        # Sigma=11 accounts for the volatility of the 2026 parity environment
        spread = norm.ppf(p) * 11 
        return round(spread * 2) / 2

    def get_vitals(self, t1, t2):
        f_path = f"{self.proc_path}/{self.gender}_full_features_2026.csv"
        feats = pd.read_csv(f_path).set_index('TeamID')
        
        pace = (feats.loc[t1, 'adjt'] + feats.loc[t2, 'adjt']) / 2
        eff_1 = (feats.loc[t1, 'adjoe'] + feats.loc[t2, 'adjde']) / 2
        eff_2 = (feats.loc[t2, 'adjoe'] + feats.loc[t1, 'adjde']) / 2
        
        score_1 = int(round(eff_1 * (pace / 100)))
        score_2 = int(round(eff_2 * (pace / 100)))
        return score_1, score_2, round((score_1 + score_2) * 2) / 2

    def display_scoreboard(self, t1, t2, t1_name, t2_name, t1_seed, t2_seed):
        sub = pd.read_csv(self.sub_path)
        id_str = f"2026_{min(t1, t2)}_{max(t1, t2)}"
        p = sub[sub['ID'] == id_str]['Pred'].values[0]
        if t1 > t2: p = 1 - p
        
        ml1, ml2 = self.prob_to_moneyline(p), self.prob_to_moneyline(1-p)
        spread = self.prob_to_spread(p)
        
        if spread > 0: s_str = f"{t1_name} -{abs(spread)}"
        elif spread < 0: s_str = f"{t2_name} -{abs(spread)}"
        else: s_str = "PK"
        
        score1, score2, total = self.get_vitals(t1, t2)
        time = self.schedule.get(t1, "TBD")
        
        print(f"\nGAME TIME : {time} EDT")
        print(f"  PROJ SCORE : {t1_name} ({t1_seed}) {score1} - {score2} {t2_name} ({t2_seed})")
        print("  " + "-"*57)
        print(f"  WIN PROB: {t1_name} {p:.2%} | {t2_name} {1-p:.2%}")
        print(f"  ML:       {t1_name} ({ml1}) | {t2_name} ({ml2})")
        print(f"  SPREAD:       {s_str}")
        print(f"  TOTAL (O/U):  {total}")
        print("-" * 65)

if __name__ == "__main__":
    matchup_list = [
        {'args': (1181, 1373, "Duke", "Siena", 1, 16), 'gender': 'M'},
        {'args': (1314, 1433, "UNC", "VCU", 6, 11), 'gender': 'M'},
        {'args': (1116, 1218, "Arkansas", "Hawaii", 4, 13), 'gender': 'M'},
        {'args': (3163, 3447, "UConn", "UTSA", 1, 16), 'gender': 'W'}
    ]

    m_sched = VegasSimulator('M').schedule
    w_sched = VegasSimulator('W').schedule
    full_sched = {**m_sched, **w_sched}

    sorted_matchups = sorted(matchup_list, key=lambda x: full_sched.get(x['args'][0], "99:99"))
    sims = {'M': VegasSimulator('M'), 'W': VegasSimulator('W')}

    # Updated header with March 19 date
    print("\n" + "="*12 + " THURSDAY, MARCH 19, 2026 TOURNAMENT SCOREBOARD " + "="*12)
    for m in sorted_matchups:
        sims[m['gender']].display_scoreboard(*m['args'])