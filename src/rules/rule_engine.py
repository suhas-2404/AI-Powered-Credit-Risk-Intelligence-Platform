def assign_risk(probability):

    if probability >= 0.70:
        return "High Risk"

    elif probability >= 0.30:
        return "Medium Risk"

    else:
        return "Low Risk"
    
def get_business_rules(customer_data, probability):

    rules = []

    # Rule 1
    if probability >= 0.70:
        rules.append(
            "Predicted default probability is above 70%"
        )

    # Rule 2
    if customer_data["NAME_EDUCATION_TYPE"] == "Lower secondary":
        rules.append(
            "Applicant has Lower Secondary education"
        )

    # Rule 3
    if customer_data["CODE_GENDER"] == "M":
        rules.append(
            "Male applicants historically show higher default rates"
        )

    # Rule 4
    if customer_data["AMT_CREDIT"] > 800000:
        rules.append(
            "Requested credit amount is high"
        )

    return rules

    