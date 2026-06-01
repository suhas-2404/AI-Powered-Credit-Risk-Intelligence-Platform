import os
import streamlit as st

st.title("📈 Explainability")

image_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "documents",
    "feature_importance.png"
)

image_path = os.path.abspath(image_path)

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.error(f"Image not found: {image_path}")