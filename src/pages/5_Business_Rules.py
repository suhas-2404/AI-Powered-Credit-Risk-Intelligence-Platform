import streamlit as st

st.title("📜 Business Rules")

rules = [
    "Lower Secondary Education → Higher Risk",
    "Male Applicants → Higher Risk",
    "Credit Amount > 800000 → Higher Risk",
    "Probability > 70% → High Risk"
]

st.subheader("Triggered Rules")

for rule in rules:
    st.info(rule)