import pandas as pd

def get_eligible_vaccines(patient_profile, vaccine_data):
    """
    Filters vaccines based on age, health conditions, and travel plans.
    """
    age = patient_profile["age"]
    conditions = [c.strip().lower() for c in patient_profile["health_conditions"]]
    travel = [t.strip().lower() for t in patient_profile["travel_plans"]]

    # Filter by age
    eligible = vaccine_data[
        (vaccine_data["age_min"] <= age) & (vaccine_data["age_max"] >= age)
    ].copy()

    # Exclude vaccines contraindicated for health conditions
    for condition in conditions:
        if condition != "none":
            eligible = eligible[
                ~eligible["contraindications"].str.lower().str.contains(condition, na=False)
            ]

    # Include travel-based vaccines
    travel_vaccines = vaccine_data[
        vaccine_data["recommended_for"].str.lower().str.contains("|".join(travel), na=False)
    ]

    # Merge without duplicates
    eligible = pd.concat([eligible, travel_vaccines]).drop_duplicates(subset=["vaccine"])

    return eligible
