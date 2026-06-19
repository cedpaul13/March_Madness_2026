import pandas as pd
import numpy as np
import os

class FinalEnsemble:
    def __init__(self):
        # 2026 Verified Injury/Roster Deductions
        # Duke: -6.5% (Caleb Foster injury - loss of primary ball handler)
        # UNC: -11.0% (Caleb Wilson injury - loss of rim protection/length)
        # Michigan: -3.0% (Cason injury - rotation depth)
        self.roster_impact = {
            1181: -0.065, 
            1314: -0.11,
            1276: -0.03
        }
        
        # NIL/Pedigree 'Chalk' Anchor (Top-K Floor)
        # Ensures blue-bloods don't drop below a talent floor against mid-majors
        self.blue_blood_ids = [1116, 1163, 1242, 1181, 1211, 3163, 3376, 3261]

    def finalize_submission(self, sub_path):
        print("Finalizing Stacked Ensemble with 2026 Guardrails...")
        df = pd.read_csv(sub_path)

        def apply_guardrails(row):
            parts = row['ID'].split('_')
            t1, t2 = int(parts[1]), int(parts[2])
            prob = row['Pred']

            # 1. Apply Injury Taxes
            for tid, tax in self.roster_impact.items():
                if t1 == tid: prob += tax # Negative tax = reduction
                if t2 == tid: prob -= tax # Team 2 injury = boost for Team 1

            # 2. Blue-Blood 'Top-K' Talent Anchor
            # If a Blue Blood is a heavy favorite (>85%), cap the upset risk
            if t1 in self.blue_blood_ids and prob > 0.85:
                prob = max(prob, 0.92)
            if t2 in self.blue_blood_ids and prob < 0.15:
                prob = min(prob, 0.08)

            return np.clip(prob, 0.01, 0.99)

        df['Pred'] = df.apply(apply_guardrails, axis=1)
        
        os.makedirs("submissions", exist_ok=True)
        final_path = os.path.join("submissions", "submission_2026_FINAL_PRO_STACKED.csv")
        df.to_csv(final_path, index=False)
        print(f"PIPELINE COMPLETE. Final submission ready: {final_path}")

if __name__ == "__main__":
    FinalEnsemble().finalize_submission(os.path.join("submissions", "submission_2026_momentum.csv"))
