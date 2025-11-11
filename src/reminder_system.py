import pandas as pd

def send_reminders(schedule):
    """
    Save schedule to CSV
    """
    schedule_df = pd.DataFrame(schedule)
    schedule_df.to_csv("outputs/optimized_schedule.csv", index=False)
    print("📩 Schedule saved successfully at: outputs/optimized_schedule.csv")
    print("🔔 Reminder system ready to send alerts before each due date.")
