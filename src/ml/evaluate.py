from sklearn.metrics import (
    roc_auc_score,
    classification_report,
    confusion_matrix
)

def evaluate_model(model, X_test, y_test):

    y_prob = model.predict_proba(X_test)[:, 1]

    roc_auc = roc_auc_score(
        y_test,
        y_prob
    )

    print(
        f"ROC-AUC: {roc_auc:.3f}"
    )

    return roc_auc


if __name__ == "__main__":

    print("Evaluation module")