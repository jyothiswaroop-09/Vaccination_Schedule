# 🧠 Vaccination Schedule Optimizer

An intelligent system that generates personalized vaccination schedules based on **age, health conditions, travel plans, and local disease outbreaks**. The tool prioritizes vaccines, optimizes scheduling, and provides reminders to help individuals plan their immunizations effectively.

---

## **Project Overview**

Vaccination planning can be complex due to different age recommendations, health conditions, travel requirements, and local outbreaks. This project provides a **personalized and optimized vaccination schedule** for individuals, ensuring safety and timely immunizations.

---

## **Features**

- ✅ Personalized vaccine recommendations based on age and health conditions  
- ✅ Travel-specific vaccine prioritization  
- ✅ Local outbreak risk assessment  
- ✅ Priority scoring system for optimal scheduling  
- ✅ Schedule generation with dose intervals considered  
- ✅ Reminders saved to CSV for tracking  
- ✅ Web interface using **Flask**  

---

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

## Skills Demonstrated
```
*AI/ML: Priority scoring, outbreak risk modeling, ML-based adjustments
*Critical Thinking: Balancing individual protection vs. population immunity
*Problem Solving: Handling complex scheduling constraints and contraindications
*Modular Structure: Clear separation of database, eligibility, priority, and schedule generation
*Clear Architecture: Pipeline from patient profile → eligibility → priority → schedule → reminders
```
## Future Enhancements
```
*Add a detailed explanation for each vaccine recommendation
*Email/SMS reminders for scheduled vaccines
*Integration with public health APIs for real-time outbreak data
*Enhanced ML modeling for better priority prediction
```
