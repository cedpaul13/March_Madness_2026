import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
import os
import importlib.util

# --- Dynamic Module Loading ---
def get_loader():
    spec = importlib.util.spec_from_file_location("data_loader_01", "src/01_data_loader.py")
    dl_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dl_mod)
    return dl_mod.DataLoader

DataLoader = get_loader()

class GeospatialEngine:
    def __init__(self, gender='M'):
        self.gender = gender
        self.raw_path = "data/raw"
        
        # 2026 Verified Men's First Round Pod Locations
        self.pods_2026 = {
            'Buffalo': (42.8864, -78.8784),
            'Greenville': (34.8526, -82.3940),
            'Oklahoma City': (35.4676, -97.5164),
            'Portland': (45.5152, -122.6784),
            'Tampa': (27.9506, -82.4572),
            'Philadelphia': (39.9526, -75.1652),
            'San Diego': (32.7157, -117.1611),
            'St. Louis': (38.6270, -90.1994)
        }

    def _get_approx_team_locs(self):
        """Calculates home coordinates using State-center centroids."""
        state_coords = {
            'AL': (32.3182, -86.9023), 'AZ': (34.0489, -111.0937), 'AR': (35.2010, -91.8318),
            'CA': (36.7783, -119.4179), 'CT': (41.6032, -73.0877), 'FL': (27.6648, -81.5158),
            'GA': (32.1656, -82.9001), 'IL': (40.6331, -89.3985), 'IN': (40.2672, -86.1349),
            'IA': (41.8780, -93.0977), 'KS': (39.0119, -98.4842), 'KY': (37.8393, -84.2700),
            'LA': (30.9843, -91.9623), 'MI': (44.3148, -85.6024), 'MS': (32.3547, -89.3985),
            'MO': (37.9643, -91.8318), 'NC': (35.7596, -79.0193), 'NE': (41.1254, -98.2681),
            'NY': (40.7128, -74.0060), 'OH': (40.4173, -82.9071), 'OK': (35.0078, -97.0929),
            'PA': (41.2033, -77.1945), 'SC': (33.8361, -81.1637), 'TN': (35.5175, -86.5804),
            'TX': (31.9686, -99.9018), 'VA': (37.4316, -78.6569), 'WA': (47.7511, -120.7401)
        }
        game_path = os.path.join(self.raw_path, f"{self.gender}GameCities.csv")
        cities = pd.read_csv(os.path.join(self.raw_path, "Cities.csv"))
        game_cities = pd.read_csv(game_path)
        
        all_visits = pd.concat([
            game_cities[['WTeamID', 'CityID']].rename(columns={'WTeamID': 'TeamID'}),
            game_cities[['LTeamID', 'CityID']].rename(columns={'LTeamID': 'TeamID'})
        ])
        home_cities = all_visits.groupby('TeamID')['CityID'].agg(lambda x: x.value_counts().index[0]).reset_index()
        home_cities = home_cities.merge(cities, on='CityID')
        
        home_cities['Lat'] = home_cities['State'].map(lambda s: state_coords.get(s, (39.8, -98.5))[0])
        home_cities['Lng'] = home_cities['State'].map(lambda s: state_coords.get(s, (39.8, -98.5))[1])
        return home_cities.set_index('TeamID')[['Lat', 'Lng']]

    def haversine(self, lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        return 2 * asin(sqrt(sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)**2)) * 3956

    def _get_2026_pod_map(self, seeds, team_locs):
        """Constructs the mapping of Team to First Round coordinates."""
        # Ensure SeedNum exists for logic gate
        seeds['SeedNum'] = seeds['Seed'].str.extract('(\d+)').astype(int)
        
        if self.gender == 'W':
            # Women's: Top 4 seeds in each region host on campus
            hosts = seeds[seeds['SeedNum'] <= 4]['TeamID'].tolist()
            return {tid: (team_locs.loc[tid, 'Lat'], team_locs.loc[tid, 'Lng']) 
                    for tid in hosts if tid in team_locs.index}
        
        # Men's Pod Mapping
        return {
            1181: self.pods_2026['Buffalo'],       # Duke
            1112: self.pods_2026['San Diego'],     # Arizona
            1345: self.pods_2026['St. Louis'],     # Purdue
            1222: self.pods_2026['Tampa'],         # Houston
            1116: self.pods_2026['Oklahoma City'], # Arkansas
            1211: self.pods_2026['Portland'],      # Gonzaga
            1163: self.pods_2026['Buffalo'],       # UConn
        }

    def process_submission(self, df, seeds):
        print(f"Applying travel bias for {self.gender}...")
        team_locs = self._get_approx_team_locs()
        pod_map = self._get_2026_pod_map(seeds, team_locs)

        def calculate_bias(row):
            parts = row['ID'].split('_')
            t1, t2 = int(parts[1]), int(parts[2])
            
            # Determine if IDs belong to current gender
            is_men = t1 < 2000
            if (self.gender == 'M' and not is_men) or (self.gender == 'W' and is_men):
                return row['Pred']

            prob = row['Pred']
            for tid in [t1, t2]:
                if tid in pod_map and tid in team_locs.index:
                    target = pod_map[tid]
                    # Target is a tuple (Lat, Lng), home is a Series with labels 'Lat', 'Lng'
                    dist = self.haversine(team_locs.loc[tid, 'Lat'], team_locs.loc[tid, 'Lng'], 
                                          target[0], target[1])
                    
                    penalty = (dist / 1000) * 0.015 # -1.5% per 1000 miles
                    boost = 0.025 if dist < 150 else 0
                    
                    if tid == t1: prob = (prob + boost) - penalty
                    else: prob = (prob - boost) + penalty
            return np.clip(prob, 0.01, 0.99)

        df['Pred'] = df.apply(calculate_bias, axis=1)
        return df

if __name__ == "__main__":
    master_sub = pd.read_csv("submission_2026_raw.csv")
    for g in ['M', 'W']:
        loader = DataLoader(g)
        seeds = loader.load_seeds()
        engine = GeospatialEngine(g)
        master_sub = engine.process_submission(master_sub, seeds)
    
    out_file = "submission_2026_geospatial.csv"
    master_sub.to_csv(out_file, index=False)
    print(f"\nFinal Geospatial submission saved to {out_file}")