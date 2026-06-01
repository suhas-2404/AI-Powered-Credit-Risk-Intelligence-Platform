import sqlite3
import pandas as pd
import os

def run_query(query):

    db_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "sql",
        "credit_risk.db"
    )

    conn = sqlite3.connect(db_path)

    result = pd.read_sql(query, conn)

    conn.close()

    return result