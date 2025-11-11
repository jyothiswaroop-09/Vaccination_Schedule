import pandas as pd

def load_vaccine_data(csv_path="data/vaccine_database.csv"):
    """
    Load vaccine database CSV.
    Expected columns: vaccine, vaccine_name, age_min, age_max, dose_interval_days, contraindications, recommended_for
    """
    df = pd.read_csv(csv_path)
    df.fillna("None", inplace=True)
    return df
