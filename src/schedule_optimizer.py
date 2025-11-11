from datetime import datetime, timedelta
import random

def generate_schedule(prioritized_vaccines, start_date=None):
    """
    Generate vaccination schedule:
    - Higher priority vaccines scheduled first
    - Subsequent vaccines scheduled with a small gap (7-14 days)
    - Dates are near each other

    prioritized_vaccines: list of dicts with keys:
        - vaccine_name
        - priority
    start_date: optional datetime.date to start schedule from today by default
    """
    if start_date is None:
        start_date = datetime.now().date()

    schedule = []
    current_date = start_date

    for vaccine in prioritized_vaccines:
        schedule.append({
            "vaccine_name": vaccine.get("vaccine_name", "Unknown"),
            "date": current_date,
            "priority": round(vaccine.get("priority", 0), 2)
        })

        # Add 7-14 days gap for next vaccine
        gap_days = random.randint(7, 14)
        current_date += timedelta(days=gap_days)

    return schedule
