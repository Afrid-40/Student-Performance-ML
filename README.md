# 🎓 Student Performance Predictor

A Machine Learning regression project that predicts a student's final academic score based on study habits, attendance, previous performance, sleep, assignment completion, and extracurricular activities.

Built with **Python, Scikit-Learn, and Streamlit**.

---

## 🚀 Features

- 📊 Synthetic student performance dataset with 1,000 records
- 🔍 Exploratory Data Analysis
- 🤖 Multiple regression models
- 📈 Model performance comparison
- 🎯 Final score prediction
- 🖥️ Interactive Streamlit dashboard
- 💾 Saved trained ML model using Joblib

---

## 🧠 Machine Learning Models

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| **Linear Regression** | **2.91** | **3.69** | **0.8785** |
| Random Forest | 3.53 | 4.44 | 0.8244 |
| Decision Tree | 4.92 | 6.07 | 0.6719 |

### 🏆 Best Model

**Linear Regression**

- MAE: **2.91**
- RMSE: **3.69**
- R² Score: **87.85%**

---

## 📊 Input Features

The model uses:

- Study Hours
- Attendance
- Previous Exam Score
- Sleep Hours
- Assignment Completion
- Extracurricular Activities

### Target

**Final Score (0–100)**

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

---

## 📁 Project Structure

```text
STUDENT-PERFORMANCE-ML/
│
├── app/
│   └── app.py
│
├── data/
│   ├── generate_data.py
│   └── student_performance.csv
│
├── models/
│   └── student_performance_model.pkl
│
├── notebooks/
│   └── student_performance.ipynb
│
├── src/
│   └── predict.py
│
├── .gitignore
├── requirements.txt
└── README.md