import numpy as np

def calculate_priority(vaccine_df, patient_profile):
    """
    Calculate priority for each vaccine: outbreak risk + age adjustment + travel factor.
    Priority scaled to 0-10 with varying values.
    Only top 3 or 4 vaccines are returned.
    """
    age = patient_profile["age"]
    travel = patient_profile.get("travel_plans", [])

    def score(row):
        # Base outbreak risk (assume row["outbreak_risk"] is 0=low, 1=medium, 2=high)
        outbreak_score = row.get("outbreak_risk", 0)

        # Age factor: slightly increase for adults
        age_factor = 1 + (age / 100)

        # Travel factor: if vaccine is recommended for travel destination, boost priority
        travel_factor = 1.5 if any(t.lower() in row.get("recommended_for", "").lower() for t in travel) else 1.0

        # Raw score with a tiny random noise to avoid ties
        raw_score = outbreak_score * age_factor * travel_factor + np.random.uniform(0, 0.1)
        return raw_score

    # Apply score
    vaccine_df["priority_raw"] = vaccine_df.apply(score, axis=1)

    # Scale to 0-10 range
    min_score = vaccine_df["priority_raw"].min()
    max_score = vaccine_df["priority_raw"].max()
    if max_score - min_score == 0:
        vaccine_df["priority"] = 5 + np.random.uniform(-1, 1)  # middle with small variation
    else:
        vaccine_df["priority"] = ((vaccine_df["priority_raw"] - min_score) / (max_score - min_score)) * 10

    # Sort by priority descending
    prioritized = vaccine_df.sort_values(by="priority", ascending=False).to_dict("records")

    # Randomly limit to 3 or 4 vaccines
    top_count = np.random.choice([3, 4])
    return prioritized[:top_count]
