import pandas as pd
import numpy as np
import os
import importlib.util
import re

# --- Dynamic Module Loading to bypass numeric filename restriction ---
def get_loader():
    spec = importlib.util.spec_from_file_location("data_loader_01", "src/01_data_loader.py")
    dl_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dl_mod)
    return dl_mod.DataLoader

DataLoader = get_loader()

class FeatureEngineer:
    def __init__(self, gender='M'):
        self.gender = gender
        self.proc_path = "data/processed"
        self.raw_path = "data/raw"
        
        # High-Rigor Coach Map with full documentation
        if gender == 'M':
            self.coach_map = {
                1116: 61, # John Calipari (Arkansas)
                1163: 18, # Dan Hurley (UConn)
                1242: 52, # Bill Self (Kansas)
                1345: 28, # Matt Painter (Purdue)
                1222: 38, # Kelvin Sampson (Houston)
                1211: 44, # Mark Few (Gonzaga)
                1112: 12, # Tommy Lloyd (Arizona)
                1385: 56, # Rick Pitino (St John's)
                1181: 4,  # Jon Scheyer (Duke)
                1314: 33, # Hubert Davis (UNC)
                1120: 18, # Bruce Pearl (Auburn)    
            }
        else:
            self.coach_map = {
                3163: 125, # Geno Auriemma (UConn)
                3437: 52,  # Dawn Staley (South Carolina)
                3261: 58,  # Kim Mulkey (LSU)
                3400: 42,  # Vic Schaefer (Texas)
                3257: 40,  # Jeff Walz (Louisville)
                3323: 15,  # Niele Ivey (Notre Dame)
                3417: 22,  # Cori Close (UCLA)
                3234: 5    # Jan Jensen (Iowa)
            }

    def build_full_matrix(self, results, seeds, trank):
        print(f"Engineering FULL {self.gender} D1 Matrix (2026)...")
        
        # 1. Load Teams Source of Truth
        teams_df = pd.read_csv(os.path.join(self.raw_path, f"{self.gender}Teams.csv"))
        
        # Rigorous check for column existence (M vs W discrepancy)
        if 'LastD1Season' in teams_df.columns:
            base_teams = teams_df[teams_df['LastD1Season'] == 2026][['TeamID', 'TeamName']]
        else:
            # For Women's data, assume all teams in the provided list are active for the current cycle
            base_teams = teams_df[['TeamID', 'TeamName']]
        
        # 2. Join Barttorvik Stats
        features = base_teams.merge(trank, on='TeamID', how='left')
        
        # 3. Impute Missing Stats (For teams not in Trank)
        cols_to_fill = ['adjoe', 'adjde', 'barthag', 'adjt']
        features[cols_to_fill] = features[cols_to_fill].fillna(features[cols_to_fill].median())
        features['Talent_Density'] = features['barthag'] ** 1.5
        
        # 4. Tactical Metrics
        res_26 = results[results['Season'] == 2026].copy()
        w_agg = res_26.groupby('WTeamID').agg({'WBlk':'mean', 'WStl':'mean', 'WDR':'mean', 'WTO':'mean'}).rename(columns={'WBlk':'Blk', 'WStl':'Stl', 'WDR':'Reb', 'WTO':'TO'})
        l_agg = res_26.groupby('LTeamID').agg({'LBlk':'mean', 'LStl':'mean', 'LDR':'mean', 'LTO':'mean'}).rename(columns={'LBlk':'Blk', 'LStl':'Stl', 'LDR':'Reb', 'LTO':'TO'})
        tactical = pd.concat([w_agg, l_agg]).groupby(level=0).mean()
        
        features = features.merge(tactical, left_on='TeamID', right_index=True, how='left')
        features[['Blk', 'Stl', 'Reb', 'TO']] = features[['Blk', 'Stl', 'Reb', 'TO']].fillna(features[['Blk', 'Stl', 'Reb', 'TO']].median())
        
        # 5. Pedigree & Conference
        features['Coach_Wins'] = features['TeamID'].map(self.coach_map).fillna(1.0)
        # Handle cases where 'conf' might be NaN after the merge
        features['conf'] = features['conf'].fillna('Independent')
        conf_avgs = features.groupby('conf')['barthag'].mean().to_dict()
        features['Conf_Rating'] = features['conf'].map(conf_avgs)
        
        # 6. Seeds (Assign 17 to non-tourney teams)
        seeds['SeedNum'] = seeds['Seed'].str.extract('(\d+)').astype(int)
        features = features.merge(seeds[['TeamID', 'SeedNum']], on='TeamID', how='left').fillna({'SeedNum': 17})
        
        out_path = os.path.join(self.proc_path, f"{self.gender}_full_features_2026.csv")
        features.drop(columns=['conf', 'TeamName']).to_csv(out_path, index=False)
        print(f"Success: {len(features)} {self.gender} teams saved to {out_path}")

if __name__ == "__main__":
    for g in ['M', 'W']:
        loader = DataLoader(g)
        seeds = loader.load_seeds()
        
        # Standardized Paths
        tr_path = os.path.join("data/raw", g, "historical", "trank_2026.csv")
        res_path = os.path.join("data/raw", f"{g}RegularSeasonDetailedResults.csv")
        
        trank = pd.read_csv(tr_path)
        team_col = 'team' if 'team' in trank.columns else trank.columns[1]
        trank['TeamID'] = trank[team_col].apply(loader._basic_clean).map(loader.id_map)
        trank = trank.dropna(subset=['TeamID'])
        
        results = pd.read_csv(res_path)
        FeatureEngineer(g).build_full_matrix(results, seeds, trank)