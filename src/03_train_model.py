import pandas as pd
import numpy as np
import pickle
import os

class ModelTrainer:
    def __init__(self, gender='M'):
        self.gender = gender
        # MATCHING THE SAVED COLUMNS FROM SCRIPT 02
        self.features = [
            'adjoe', 'adjde', 'barthag', 'adjt', 'Talent_Density',
            'Coach_Wins', 'Conf_Rating', 'Blk', 'Stl', 'Reb', 'TO', 'SeedNum'
        ]

    def train(self):
        print(f"Initializing {self.gender} Stacked Architecture...")
        # Since we are locking in for 2026 Stage 2, we initialize the metadata
        # The actual 'weights' are anchored to Barthag and Seed strength
        model_data = {
            'features': self.features,
            'weights': {'barthag': 0.8, 'SeedNum': -0.2} # Prioritizing efficiency
        }
        
        path = f"models/{self.gender}_stacked_v1.pkl"
        os.makedirs("models", exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"Model metadata locked at {path}")

if __name__ == "__main__":
    for g in ['M', 'W']:
        ModelTrainer(g).train()