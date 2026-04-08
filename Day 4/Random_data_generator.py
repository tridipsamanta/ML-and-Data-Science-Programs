import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ---------- Step 1: Generate fake data ----------
np.random.seed(None)  # random every run

data = {
    "student_id": range(1, 21),
    "study_hours": np.random.randint(1, 10, 20),
    "exam_score": np.random.randint(40, 100, 20)
}

df = pd.DataFrame(data)

print("\n📊 Student Data (DataFrame):")
print(df)

# ---------- Step 2: Analysis ----------
summary_df = pd.DataFrame({
    "Metric": ["Average Study Hours", "Average Exam Score", "Correlation"],
    "Value": [
        df["study_hours"].mean(),
        df["exam_score"].mean(),
        df["study_hours"].corr(df["exam_score"])
    ]
})

print("\n📈 Summary (DataFrame):")
print(summary_df)

# ---------- Step 3: Save CSV with timestamp ----------
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_filename = f"day4_student_data_{timestamp}.csv"
df.to_csv(csv_filename, index=False)

# ---------- Step 4: Visualization using pyplot ----------
plt.figure()
plt.bar(summary_df["Metric"], summary_df["Value"])
plt.title("Data Science Day 4 Summary")
plt.ylabel("Value")
plt.xticks(rotation=10)
plt.tight_layout()
plt.show()

print(f"\n✅ New CSV created: {csv_filename}")
