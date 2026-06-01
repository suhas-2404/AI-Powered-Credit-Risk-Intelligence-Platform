import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EDA Dashboard",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis Dashboard")

st.markdown(
    "Key insights and statistics from the Credit Risk dataset."
)

# ==========================
# Top Metrics
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Applications",
        "307,511"
    )

with col2:
    st.metric(
        "Default Rate",
        "8.07%"
    )

with col3:
    st.metric(
        "Model ROC-AUC",
        "0.753"
    )

st.divider()

# ==========================
# Default Distribution
# ==========================

st.subheader("📈 Loan Default Distribution")

target_df = pd.DataFrame({
    "Class": ["Non-Default", "Default"],
    "Count": [282686, 24825]
})

fig_target = px.bar(
    target_df,
    x="Class",
    y="Count",
    text="Count",
    title="Default vs Non-Default Customers"
)

st.plotly_chart(
    fig_target,
    use_container_width=True
)

# ==========================
# Gender Analysis
# ==========================

st.subheader("👨 Gender-wise Default Rate")

gender_df = pd.DataFrame({
    "Gender": ["Female", "Male"],
    "Default Rate (%)": [7.00, 10.14]
})

fig_gender = px.bar(
    gender_df,
    x="Gender",
    y="Default Rate (%)",
    text="Default Rate (%)",
    title="Gender vs Default Rate"
)

st.plotly_chart(
    fig_gender,
    use_container_width=True
)

# ==========================
# Education Analysis
# ==========================

st.subheader("🎓 Education-wise Default Rate")

education_df = pd.DataFrame({
    "Education": [
        "Academic Degree",
        "Higher Education",
        "Incomplete Higher",
        "Lower Secondary",
        "Secondary Special"
    ],
    "Default Rate (%)": [
        1.83,
        5.35,
        8.48,
        10.93,
        8.94
    ]
})

fig_education = px.bar(
    education_df,
    x="Education",
    y="Default Rate (%)",
    text="Default Rate (%)",
    title="Education Level vs Default Rate"
)

st.plotly_chart(
    fig_education,
    use_container_width=True
)

# ==========================
# Income Insights
# ==========================

st.subheader("💰 Income Analysis")

income_df = pd.DataFrame({
    "Customer Type": [
        "Non-Default",
        "Default"
    ],
    "Average Income": [
        169078,
        165612
    ]
})

fig_income = px.bar(
    income_df,
    x="Customer Type",
    y="Average Income",
    text="Average Income",
    title="Average Income by Customer Type"
)

st.plotly_chart(
    fig_income,
    use_container_width=True
)

# ==========================
# Age Insights
# ==========================

st.subheader("👥 Age Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Age",
        "43.9 Years"
    )

with col2:
    st.metric(
        "Minimum Age",
        "20.5 Years"
    )

with col3:
    st.metric(
        "Maximum Age",
        "69.1 Years"
    )

# ==========================
# Business Insights
# ==========================

st.subheader("📋 Key Business Insights")

st.success(
    """
    ✅ Only 8.07% of applicants defaulted on loans.

    ✅ Male applicants show a higher default rate (10.14%)
    compared to female applicants (7.00%).

    ✅ Lower Secondary education has the highest default rate (10.93%).

    ✅ Academic Degree holders have the lowest default rate (1.83%).

    ✅ Average applicant age is 43.9 years.

    ✅ XGBoost achieved a ROC-AUC score of 0.753.
    """
)

# ==========================
# Project Summary
# ==========================

st.subheader("🏦 Credit Risk Project Summary")

summary_df = pd.DataFrame({
    "Metric": [
        "Dataset Rows",
        "Initial Features",
        "Final Features",
        "Default Rate",
        "Best Model",
        "ROC-AUC Score"
    ],
    "Value": [
        "307,511",
        "122",
        "80",
        "8.07%",
        "XGBoost",
        "0.753"
    ]
})

st.dataframe(
    summary_df,
    use_container_width=True
)