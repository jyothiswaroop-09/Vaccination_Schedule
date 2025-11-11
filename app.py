from flask import Flask, render_template, request
from src.vaccine_database import load_vaccine_data
from src.eligibility_checker import get_eligible_vaccines
from src.outbreak_model import get_outbreak_risk
from src.priority_scorer import calculate_priority
from src.schedule_optimizer import generate_schedule
from src.reminder_system import send_reminders

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    schedule = None
    if request.method == "POST":
        age = int(request.form.get("age"))
        health_conditions = request.form.get("health_conditions", "").split(",")
        travel_plans = request.form.get("travel_plans", "").split(",")
        location = request.form.get("location", "").strip()

        patient_profile = {
            "age": age,
            "health_conditions": [c.strip().lower() for c in health_conditions],
            "travel_plans": [t.strip().lower() for t in travel_plans],
            "location": location.lower()
        }

        # Load vaccine data
        vaccine_data = load_vaccine_data("data/vaccine_database.csv")

        # Filter eligible vaccines
        eligible_vaccines = get_eligible_vaccines(patient_profile, vaccine_data)

        # Assign outbreak risk
        vaccines_with_risk = get_outbreak_risk(patient_profile["location"], eligible_vaccines)

        # Calculate priority and get top vaccines
        prioritized = calculate_priority(vaccines_with_risk, patient_profile)

        # Generate schedule
        schedule = generate_schedule(prioritized)

        # Save schedule to CSV
        send_reminders(schedule)

    return render_template("index.html", schedule=schedule)

if __name__ == "__main__":
    app.run(debug=True)
