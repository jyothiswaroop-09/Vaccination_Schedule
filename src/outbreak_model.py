import pandas as pd

def get_outbreak_risk(location, eligible_vaccines, outbreak_csv="data/outbreak_data.csv"):
    """
    Assign risk score to vaccines based on outbreak severity.
    """
    outbreak_data = pd.read_csv(outbreak_csv)
    outbreak_data.fillna("low", inplace=True)

    risk_map = {"low": 1, "medium": 3, "high": 5}

    # Default risk
    eligible_vaccines["outbreak_risk"] = 1

    for idx, row in eligible_vaccines.iterrows():
        match = outbreak_data[
            (outbreak_data["disease"].str.lower() == row["vaccine_name"].lower()) &
            ((outbreak_data["region"].str.lower() == location.lower()) | (outbreak_data["region"].str.lower() == "global"))
        ]
        if not match.empty:
            eligible_vaccines.at[idx, "outbreak_risk"] = risk_map.get(match.iloc[0]["severity"].lower(), 1)

    return eligible_vaccines
