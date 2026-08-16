import joblib
import pandas as pd
import os


# Load trained model
model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "student_performance_model.pkl"
)

model = joblib.load(model_path)


def predict_score(
    study_hours,
    attendance,
    previous_score,
    sleep_hours,
    assignment_completion,
    extracurricular
):
    student = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_score": [previous_score],
        "sleep_hours": [sleep_hours],
        "assignment_completion": [assignment_completion],
        "extracurricular": [extracurricular]
    })

    prediction = model.predict(student)[0]

    return prediction


if __name__ == "__main__":

    score = predict_score(
        study_hours=6,
        attendance=85,
        previous_score=75,
        sleep_hours=7,
        assignment_completion=90,
        extracurricular=1
    )

    print(f"Predicted Final Score: {score:.2f}")