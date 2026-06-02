import os
import streamlit as st

st.title("📈 Explainability")

# Feature Importance Chart
image_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "documents",
    "feature_importance.png"
)

image_path = os.path.abspath(image_path)

if os.path.exists(image_path):
    st.subheader("Feature Importance Analysis")
    st.image(
        image_path,
        use_container_width=True
    )
else:
    st.error(f"Image not found: {image_path}")

# Top Features
st.subheader("Top Influential Features")

st.markdown("""
1. **EXT_SOURCE_2**  
2. **EXT_SOURCE_3**  
3. **AMT_CREDIT**  
4. **AMT_INCOME_TOTAL**  
5. **DAYS_BIRTH**
""")

# Sample Explanation
st.subheader("Sample Prediction Explanation")

st.metric(
    label="Risk Probability",
    value="12%"
)

st.success("🟢 Low Risk")

st.markdown("""
### Customer Profile

- Income: ₹150,000
- Credit Amount: ₹500,000
- Education: Higher Education

### Factors Influencing Prediction

✅ Stable Income

✅ Moderate Credit Amount

✅ Higher Education

### Final Classification

**Low Risk**
""")

# Explainability Summary
st.info("""
The model's predictions are influenced by financial,
demographic, and external credit score features.

Feature importance analysis helps identify the most
significant variables contributing to credit risk.
""")