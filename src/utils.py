import pandas as pd
import os

def save_schedule(schedule_df: pd.DataFrame, path: str):
    """
    Saves the generated vaccination schedule to CSV.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    schedule_df.to_csv(path, index=False)
