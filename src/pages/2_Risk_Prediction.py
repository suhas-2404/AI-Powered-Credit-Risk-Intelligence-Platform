import streamlit as st

st.title("🤖 Credit Risk Prediction")

income = st.number_input(
    "Income",
    value=150000
)

credit = st.number_input(
    "Credit Amount",
    value=500000
)

education = st.selectbox(
    "Education",
    [
        "Higher education",
        "Secondary / secondary special",
        "Lower secondary"
    ]
)

if st.button("Predict Risk"):

    score = 0

    if credit > 800000:
        score += 30

    if income < 100000:
        score += 30

    if education == "Lower secondary":
        score += 20

    probability = min(score / 100, 0.95)

    if probability >= 0.70:
        risk = "High Risk"

    elif probability >= 0.30:
        risk = "Medium Risk"

    else:
        risk = "Low Risk"

    st.metric(
        "Risk Probability",
        f"{probability*100:.1f}%"
    )

    if risk == "High Risk":
      st.error(f"Risk Category: {risk}")

    elif risk == "Medium Risk":
      st.warning(f"Risk Category: {risk}")

    else:
      st.success(f"Risk Category: {risk}")

