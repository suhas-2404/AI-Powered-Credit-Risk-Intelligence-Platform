import streamlit as st
import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

sys.path.append(project_root)

from src.talk_to_data.nl_to_sql import generate_sql
from src.talk_to_data.query_runner import run_query

st.title("💬 Talk to Data")

question = st.text_input(
    "Ask a question about the credit risk data"
)

if st.button("Generate Answer"):

    try:

        sql_query = generate_sql(question)

        st.subheader("Generated SQL")

        st.code(sql_query, language="sql")

        result = run_query(sql_query)

        st.subheader("Query Result")

        if result.shape == (1, 1):

            value = result.iloc[0, 0]

            st.metric(
                "Answer",
                f"{value:,}"
            )

        else:

            st.dataframe(
                result,
                use_container_width=True
            )

    except Exception as e:

        st.error(str(e))