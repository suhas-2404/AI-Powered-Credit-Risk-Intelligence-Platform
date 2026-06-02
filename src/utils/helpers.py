def assign_risk(probability):

    if probability >= 0.70:
        return "High Risk"

    elif probability >= 0.30:
        return "Medium Risk"

    return "Low Risk"


def format_percentage(value):

    return f"{value * 100:.2f}%"