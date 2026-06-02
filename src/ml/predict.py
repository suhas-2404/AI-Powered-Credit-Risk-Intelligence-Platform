import joblib
import pandas as pd

def load_model(model_path):

    return joblib.load(model_path)


def predict_risk(model, applicant_data):

    df = pd.DataFrame([applicant_data])

    probability = model.predict_proba(df)[0][1]

    return probability


if __name__ == "__main__":

    print("Prediction module")