import pandas as pd
import os
import re

class DataLoader:
    def __init__(self, gender='M'):
        self.gender = gender
        self.raw_path = "data/raw"
        self.id_map = self._get_id_map()

    def _basic_clean(self, name):
        """Standardizes name for cross-source mapping."""
        if not isinstance(name, str) or name == "": return ""
        name = name.lower().strip()
        # Handle different apostrophe types
        name = name.replace('’', "'").replace('.', '')
        # Remove numbers (seeds/ranks)
        name = re.sub(r'\d+', '', name)
        # Surgical replacement to avoid 'Stateate' bug
        name = re.sub(r'\bst\b', 'state', name) # Replace 'st' only if it's a standalone word
        # Remove extra symbols but keep spaces/apostrophes
        name = re.sub(r'[^\w\s\']', '', name)
        return " ".join(name.split()) # Normalize whitespace

    def _get_id_map(self):
        path = os.path.join(self.raw_path, f"{self.gender}TeamSpellings.csv")
        df = pd.read_csv(path, encoding='cp1252')
        # Map cleaned spellings to TeamID
        mapping = df.set_index(df['TeamNameSpelling'].apply(self._basic_clean))['TeamID'].to_dict()
        return mapping

    def load_seeds(self):
        path = os.path.join(self.raw_path, f"2026_{self.gender}Seeds.csv")
        df = pd.read_csv(path)
        df['TeamID'] = df['TeamName'].apply(self._basic_clean).map(self.id_map)
        
        missing = df[df['TeamID'].isnull()]
        if not missing.empty:
            print(f"Warning: {len(missing)} {self.gender} teams failed to map: {missing['TeamName'].tolist()}")
        return df.dropna(subset=['TeamID'])

    def load_trank(self):
        path = os.path.join(self.raw_path, f"trank_{self.gender}_2026.csv")
        df = pd.read_csv(path)
        # Use col index 1 for 'team' if name varies
        df['TeamID'] = df['team'].apply(self._basic_clean).map(self.id_map)
        return df.dropna(subset=['TeamID']).set_index('TeamID')

    def load_kenpom(self):
        if self.gender == 'W': return None
        path = os.path.join(self.raw_path, "kenpom_stats.csv")
        df = pd.read_csv(path)
        team_col = df.columns[1]
        df['TeamID'] = df[team_col].apply(self._basic_clean).map(self.id_map)
        return df.dropna(subset=['TeamID']).set_index('TeamID')

if __name__ == "__main__":
    for g in ['M', 'W']:
        loader = DataLoader(g)
        seeds = loader.load_seeds()
        trank = loader.load_trank()
        print(f"\n--- {g} 2026 Verification ---")
        print(f"Verified Seeds Mapped: {len(seeds)}")
        print(f"Barttorvik Teams Mapped: {len(trank) if trank is not None else 0}")
        print("Status: SUCCESS" if len(seeds) >= 64 else "Status: PARTIAL FAIL")