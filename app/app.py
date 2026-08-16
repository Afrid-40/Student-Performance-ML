import os
import sys

import streamlit as st


# =========================================================
# MODEL IMPORT
# =========================================================

SRC_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "src")
)

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from predict import predict_score


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# CONSTANTS
# =========================================================

MODEL_NAME = "Linear Regression"
MODEL_R2 = 0.8785
MODEL_MAE = 2.91
MODEL_RMSE = 3.69


# =========================================================
# SESSION STATE
# =========================================================

if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "inputs" not in st.session_state:
    st.session_state.inputs = None


# =========================================================
# CUSTOM CSS
# IMPORTANT:
# This CSS is the only HTML-based section in the app.
# UI content itself uses native Streamlit components,
# which prevents raw HTML from appearing on screen.
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 8% 5%,
                rgba(220, 38, 38, 0.16),
                transparent 30%
            ),
            radial-gradient(
                circle at 92% 90%,
                rgba(127, 29, 29, 0.14),
                transparent 32%
            ),
            #070707;
        color: #f5f5f5;
    }

    [data-testid="stAppViewContainer"] {
        background: transparent;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu,
    footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1120px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ---------- TYPOGRAPHY ---------- */

    h1, h2, h3, p, label {
        font-family:
            Inter, ui-sans-serif, system-ui, -apple-system,
            BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    /* ---------- HERO ---------- */

    .hero-box {
        padding: 34px;
        margin-bottom: 26px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.09);
        background:
            linear-gradient(
                135deg,
                rgba(255, 255, 255, 0.065),
                rgba(255, 255, 255, 0.018)
            );
        box-shadow:
            0 24px 70px rgba(0, 0, 0, 0.35),
            inset 0 1px 0 rgba(255, 255, 255, 0.03);
    }

    .hero-kicker {
        color: #ef4444;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .hero-title {
        font-size: clamp(32px, 5vw, 54px);
        line-height: 1.05;
        font-weight: 900;
        letter-spacing: -2px;
        margin: 0;
        color: #ffffff;
    }

    .hero-title-accent {
        color: #ff3333;
    }

    .hero-subtitle {
        margin-top: 12px;
        color: #a1a1aa;
        font-size: 16px;
        line-height: 1.6;
        max-width: 720px;
    }

    /* ---------- SECTION HEADINGS ---------- */

    .section-kicker {
        color: #ef4444;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 4px;
    }

    /* ---------- STREAMLIT INPUTS ---------- */

    [data-testid="stSlider"] {
        padding: 4px 0 10px;
    }

    [data-testid="stSlider"] label,
    [data-testid="stSelectbox"] label {
        color: #e4e4e7 !important;
        font-weight: 650 !important;
    }

    [data-baseweb="select"] > div {
        background: #111111 !important;
        border-color: rgba(255, 255, 255, 0.12) !important;
        color: #ffffff !important;
    }

    /* ---------- BUTTONS ---------- */

    .stButton > button {
        min-height: 54px;
        border: 0;
        border-radius: 14px;
        background: linear-gradient(90deg, #b30000, #ff2d2d);
        color: #ffffff;
        font-size: 15px;
        font-weight: 800;
        letter-spacing: 0.3px;
        box-shadow: 0 12px 32px rgba(255, 0, 0, 0.16);
        transition: transform 0.18s ease, box-shadow 0.18s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 16px 40px rgba(255, 0, 0, 0.28);
        color: #ffffff;
    }

    /* Secondary button */
    .secondary-button .stButton > button {
        background: rgba(255, 255, 255, 0.055);
        border: 1px solid rgba(255, 255, 255, 0.10);
        box-shadow: none;
    }

    /* ---------- NATIVE CONTAINERS ---------- */

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 18px !important;
        border-color: rgba(255, 255, 255, 0.09) !important;
        background: rgba(255, 255, 255, 0.025) !important;
    }

    /* ---------- METRICS ---------- */

    [data-testid="stMetric"] {
        padding: 16px 18px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        background: rgba(255, 255, 255, 0.035);
    }

    [data-testid="stMetricLabel"] {
        color: #a1a1aa !important;
    }

    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-weight: 800 !important;
    }

    /* ---------- PROGRESS ---------- */

    [data-testid="stProgressBar"] {
        margin-top: 12px;
        margin-bottom: 8px;
    }

    /* ---------- ALERTS ---------- */

    [data-testid="stAlert"] {
        border-radius: 14px;
    }

    /* ---------- FOOTER ---------- */

    .footer-line {
        height: 1px;
        background: rgba(255, 255, 255, 0.07);
        margin: 42px 0 20px;
    }

    .footer-text {
        text-align: center;
        color: #71717a;
        font-size: 12px;
        line-height: 1.8;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-kicker">ML REGRESSION SYSTEM • v1.0</div>
        <div class="hero-title">
            🎓 Student <span class="hero-title-accent">Performance</span>
        </div>
        <div class="hero-subtitle">
            Predict a student's final academic score using study habits,
            attendance, previous performance, sleep, assignment completion,
            and extracurricular participation.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# STUDENT PROFILE
# =========================================================

st.markdown("### 📊 Student Profile")
st.caption("Adjust the inputs below and analyze the expected final score.")

left, right = st.columns(2, gap="large")

with left:
    study_hours = st.slider(
        "📚 Daily Study Hours",
        min_value=1.0,
        max_value=10.0,
        value=5.0,
        step=0.5,
        help="Average number of hours spent studying each day.",
    )

    attendance = st.slider(
        "📈 Attendance (%)",
        min_value=50.0,
        max_value=100.0,
        value=75.0,
        step=1.0,
        help="Overall class attendance percentage.",
    )

    previous_score = st.slider(
        "📝 Previous Exam Score",
        min_value=40.0,
        max_value=95.0,
        value=65.0,
        step=1.0,
        help="Score obtained in the previous examination.",
    )

with right:
    sleep_hours = st.slider(
        "😴 Average Sleep Hours",
        min_value=4.0,
        max_value=9.0,
        value=7.0,
        step=0.5,
        help="Average sleep duration per night.",
    )

    assignment_completion = st.slider(
        "📚 Assignment Completion (%)",
        min_value=40.0,
        max_value=100.0,
        value=70.0,
        step=1.0,
        help="Percentage of assignments completed.",
    )

    extracurricular = st.selectbox(
        "🏆 Extracurricular Activities",
        options=["No", "Yes"],
        help="Whether the student participates in extracurricular activities.",
    )

extracurricular_value = 1 if extracurricular == "Yes" else 0


# =========================================================
# INPUT SUMMARY
# =========================================================

st.markdown("### ⚡ Current Profile")

s1, s2, s3, s4, s5 = st.columns(5)

with s1:
    st.metric("Study", f"{study_hours:.1f} h")

with s2:
    st.metric("Attendance", f"{attendance:.0f}%")

with s3:
    st.metric("Previous", f"{previous_score:.0f}")

with s4:
    st.metric("Sleep", f"{sleep_hours:.1f} h")

with s5:
    st.metric("Assignments", f"{assignment_completion:.0f}%")


st.write("")


# =========================================================
# ACTIONS
# =========================================================

a1, a2 = st.columns([4, 1], gap="medium")

with a1:
    analyze = st.button(
        "🚀 ANALYZE PERFORMANCE",
        use_container_width=True,
        type="primary",
    )

with a2:
    st.markdown('<div class="secondary-button">', unsafe_allow_html=True)
    reset = st.button(
        "↻ Reset",
        use_container_width=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


if reset:
    st.session_state.prediction = None
    st.session_state.inputs = None
    st.rerun()


# =========================================================
# RUN PREDICTION
# =========================================================

if analyze:
    prediction = predict_score(
        study_hours,
        attendance,
        previous_score,
        sleep_hours,
        assignment_completion,
        extracurricular_value,
    )

    prediction = float(max(0.0, min(100.0, prediction)))

    st.session_state.prediction = prediction
    st.session_state.inputs = {
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score,
        "sleep_hours": sleep_hours,
        "assignment_completion": assignment_completion,
        "extracurricular": extracurricular,
    }


# =========================================================
# RESULTS
# =========================================================

if st.session_state.prediction is not None:

    prediction = st.session_state.prediction

    if prediction >= 90:
        status = "🌟 Excellent Performance"
        status_message = (
            "The model predicts a very strong final score. "
            "Keep the current academic routine consistent."
        )
        status_type = "success"

    elif prediction >= 75:
        status = "🟢 Good Performance"
        status_message = (
            "The predicted performance is good. "
            "Consistent study and attendance can help maintain it."
        )
        status_type = "info"

    elif prediction >= 60:
        status = "🟡 Needs Improvement"
        status_message = (
            "There is room for academic improvement. "
            "Increasing study consistency and assignment completion may help."
        )
        status_type = "warning"

    else:
        status = "🔴 High Risk"
        status_message = (
            "The predicted score is relatively low. "
            "Focus on study time, attendance, assignments, and previous weak areas."
        )
        status_type = "error"

    st.markdown("---")
    st.markdown("### 🎯 Prediction Result")

    # Main result card using native Streamlit components.
    # No HTML content is used here, so raw <div> text cannot appear.
    with st.container(border=True):

        r1, r2, r3 = st.columns([1.5, 1, 1])

        with r1:
            st.caption("PREDICTED FINAL SCORE")
            st.markdown(
                f"<h1 style='font-size:64px; margin:0; color:#ff3333;'>{prediction:.2f}</h1>",
                unsafe_allow_html=True,
            )
            st.caption("out of 100")

        with r2:
            st.metric(
                "Model",
                MODEL_NAME,
            )
            st.metric(
                "R² Score",
                f"{MODEL_R2 * 100:.2f}%",
            )

        with r3:
            st.metric(
                "MAE",
                f"{MODEL_MAE:.2f}",
            )
            st.metric(
                "RMSE",
                f"{MODEL_RMSE:.2f}",
            )

        st.progress(
            int(round(prediction)),
            text=f"Predicted performance: {prediction:.1f} / 100",
        )

        if status_type == "success":
            st.success(f"{status}\n\n{status_message}")
        elif status_type == "info":
            st.info(f"{status}\n\n{status_message}")
        elif status_type == "warning":
            st.warning(f"{status}\n\n{status_message}")
        else:
            st.error(f"{status}\n\n{status_message}")


    # =====================================================
    # PROFILE USED FOR PREDICTION
    # =====================================================

    st.markdown("### 🔍 Prediction Inputs")

    saved = st.session_state.inputs

    p1, p2, p3 = st.columns(3)

    with p1:
        st.metric("Study Hours", f"{saved['study_hours']:.1f} h")
        st.metric("Attendance", f"{saved['attendance']:.0f}%")

    with p2:
        st.metric("Previous Score", f"{saved['previous_score']:.0f}")
        st.metric("Sleep", f"{saved['sleep_hours']:.1f} h")

    with p3:
        st.metric(
            "Assignments",
            f"{saved['assignment_completion']:.0f}%",
        )
        st.metric(
            "Extracurricular",
            saved["extracurricular"],
        )


    # =====================================================
    # MODEL PERFORMANCE
    # =====================================================

    st.markdown("### 🧠 Model Performance")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "MAE",
            f"{MODEL_MAE:.2f}",
            help="Mean Absolute Error. Lower is better.",
        )

    with m2:
        st.metric(
            "RMSE",
            f"{MODEL_RMSE:.2f}",
            help="Root Mean Squared Error. Lower is better.",
        )

    with m3:
        st.metric(
            "R²",
            f"{MODEL_R2:.4f}",
            help="Coefficient of determination. Higher is better.",
        )


    # =====================================================
    # PROJECT NOTE
    # =====================================================

    st.caption(
        "Model: Linear Regression • "
        "Features: study hours, attendance, previous score, "
        "sleep, assignment completion, extracurricular activity"
    )

else:
    st.markdown("---")

    with st.container(border=True):
        st.markdown("### 👋 Ready to analyze?")
        st.write(
            "Set the student's profile above and click "
            "**Analyze Performance** to generate a prediction."
        )

        q1, q2, q3 = st.columns(3)

        with q1:
            st.metric("Training Samples", "1,000")

        with q2:
            st.metric("Features", "6")

        with q3:
            st.metric("Regression Model", "Linear")


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer-line"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="footer-text">
        🎓 STUDENT PERFORMANCE PREDICTOR<br>
        Built with Python • Scikit-Learn • Streamlit<br>
        ML Regression Mini Project • v1.0
    </div>
    """,
    unsafe_allow_html=True,
)
