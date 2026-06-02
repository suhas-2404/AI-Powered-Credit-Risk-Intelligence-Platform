import os

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "credit_risk_model.pkl"
)

DB_PATH = os.path.join(
    BASE_DIR,
    "sql",
    "credit_risk.db"
)