import numpy as np
import pandas as pd

np.random.seed(42)

n_students = 1000

study_hours = np.random.uniform(1, 10, n_students)
attendance = np.random.uniform(50, 100, n_students)
previous_score = np.random.uniform(40, 95, n_students)
sleep_hours = np.random.uniform(4, 9, n_students)
assignment_completion = np.random.uniform(40, 100, n_students)
extracurricular = np.random.randint(0, 2, n_students)

# Generate final score with some realistic relationships
final_score = (
    0.35 * previous_score
    + 2.5 * study_hours
    + 0.20 * attendance
    + 1.5 * sleep_hours
    + 0.15 * assignment_completion
    + 2.0 * extracurricular
    + np.random.normal(0, 4, n_students)
)

# Keep scores between 0 and 100
final_score = np.clip(final_score, 0, 100)

df = pd.DataFrame({
    "study_hours": np.round(study_hours, 2),
    "attendance": np.round(attendance, 2),
    "previous_score": np.round(previous_score, 2),
    "sleep_hours": np.round(sleep_hours, 2),
    "assignment_completion": np.round(assignment_completion, 2),
    "extracurricular": extracurricular,
    "final_score": np.round(final_score, 2)
})

df.to_csv("data/student_performance.csv", index=False)

print("Dataset created successfully!")
print(f"Number of students: {len(df)}")
print("\nFirst 5 rows:")
print(df.head())
print("\nDataset shape:", df.shape)