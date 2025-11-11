## 🧠 Vaccination Schedule Optimizer
### 📋 Project Overview
The Vaccination Schedule Optimizer is an intelligent system that generates personalized vaccination schedules based on:
```
👶 Age
❤️ Health conditions
✈️ Travel plans
📍 Local disease outbreaks
This system ensures individuals receive the right vaccines at the right time, balancing personal protection and population immunity.
```
## 🚀 Features
```
🧩 Eligibility Checker – Filters vaccines by age, health, and travel data
🌍 Outbreak Risk Model – Incorporates live outbreak risk for the user’s region
⚙️ Priority Scoring System – Assigns vaccine importance dynamically (0–10 scale)
📆 Schedule Optimizer – Creates smart vaccination timelines
🔔 Reminder System – Generates alerts for upcoming doses
💡 ML Model Integration – Supports predictive or adaptive modeling in ml_model.py
🌐 Flask Web Interface – Simple user interface for easy interaction
```
## 🧠 Skills Demonstrated
```
AI/ML Concepts: Priority algorithms, outbreak modeling, and data-driven scoring
Critical Thinking: Balancing protection vs. immunity and optimizing timing
Problem Solving: Handling constraints, catch-up doses, and contraindications
Modular Design: Clean separation between data, logic, and web interface
```
## **Project Structure**
```
Vaccination_Schedule_Optimizer/
│
├── data/
│ ├── vaccine_database.csv # Vaccine info: age range, contraindications, dose intervals
│ ├── outbreak_data.csv # Local and travel outbreak data
│
├── src/
│ ├── vaccine_database.py # Load and manage vaccine data
│ ├── eligibility_checker.py # Filter vaccines by age, health, and contraindications
│ ├── outbreak_model.py # Assign outbreak risk based on location
│ ├── priority_scorer.py # Calculate priority scores for vaccines
│ ├── schedule_optimizer.py # Generate vaccination schedule
│ ├── reminder_system.py # Save schedules and reminders
│ ├── ml_model.py # ML-based risk or priority modeling (optional/advanced)
│ ├── utils.py # Helper functions
│
├── outputs/
│ ├── optimized_schedule.csv # Generated vaccination schedule
│
├── templates/
│ ├── index.html # Flask web interface
│
├── app.py # Flask application
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

---

## **How It Works**

1. **User Input**:  
   - Age  
   - Health conditions (selectable from dropdown)  
   - Travel destinations  
   - Current location  

2. **Eligibility Check**:  
   - Filters vaccines based on age, health conditions, and contraindications.  

3. **Outbreak Risk Assessment**:  
   - Uses local and travel outbreak data to assign risk scores to vaccines.  

4. **Priority Scoring**:  
   - Combines outbreak risk, age factor, travel factor, and optional ML-based adjustments.  
   - Scaled to a 0–10 range to prioritize vaccines effectively.  

5. **Schedule Generation**:  
   - Assigns dates based on dose intervals.  
   - Limits to top 3–5 vaccines for clarity.  

6. **Reminders**:  
   - Saves the optimized schedule in `outputs/optimized_schedule.csv`.  

---

## **Installation**
```
1. Clone the repository:
git clone https://github.com/yourusername/Vaccination_Schedule_Optimizer.git
cd Vaccination_Schedule_Optimizer

2.Create a virtual environment:
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

3.Install dependencies:
pandas
numpy
flask
scikit-learn
openpyxl
pip install -r requirements.txt

4.Run the Flask app:
python app.py

5.Open a browser and navigate to:
http://127.0.0.1:5000/
```

## Example Output
```
✅ Vaccination Schedule:
🔹 Yellow Fever on 2025-11-11 (Priority: 10.00)
🔹 Influenza (Flu Shot) on 2025-11-21 (Priority: 7.28)
🔹 Typhoid Vaccine on 2025-11-28 (Priority: 5.92)
📩 Schedule saved at: outputs/optimized_schedule.csv
```
### Login Page
![Login Page](outputs/screenshots/Login(1).png)

### Home Page
![Home Page](outputs/screenshots/Home(2).png)

### Selection Page
![Selection Page](outputs/screenshots/Selection(3).png)

### Values Page
![Values Page](outputs/screenshots/Value(4).png)

### Output Page
![Output Page](outputs/screenshots/Output(5).png)

## 🧠 Machine Learning Module (ml_model.py)
```
This module can be used for:
Predicting outbreak severity using ML models
Training a model to dynamically adjust vaccine priority
Integrating historical data for future vaccine scheduling

*Example models you can integrate:
.Logistic Regression for outbreak prediction
.Random Forest for vaccine importance classification
.Neural Networks for adaptive vaccine planning
```
## Future Enhancements
```
*Add a detailed explanation for each vaccine recommendation
*Email/SMS reminders for scheduled vaccines
*Integration with public health APIs for real-time outbreak data
*Enhanced ML modeling for better priority prediction
```
## 👤 Author
```
Name: Jyothi Swaroop
Role: AI/ML Developer | Data Scientist
Email: [swaroop.motupalli@gmail.com]
GitHub: [(https://github.com/jyothiswaroop-09)]
LinkedIn: https://www.linkedin.com/in/jyothi-swaroop-278084338
```
