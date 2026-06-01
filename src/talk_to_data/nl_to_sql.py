import google.generativeai as genai
from dotenv import load_dotenv
import os

from src.talk_to_data.prompt_templates import SQL_PROMPT

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_sql(question):

    prompt = SQL_PROMPT.format(
        question=question
    )

    response = model.generate_content(prompt)

    sql_query = clean_sql(response.text)

    return sql_query

def clean_sql(sql_query):

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```sqlite", "")
    sql_query = sql_query.replace("```", "")

    sql_query = sql_query.replace("default", "TARGET")
    sql_query = sql_query.replace("Default", "TARGET")
    sql_query = sql_query.replace("DEFAULT", "TARGET")

    return sql_query.strip()