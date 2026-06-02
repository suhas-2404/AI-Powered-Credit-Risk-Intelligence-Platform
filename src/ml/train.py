import joblib
from xgboost import XGBClassifier

def train_model(X_train, y_train):

    model = XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        eval_metric="logloss",
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def save_model(model, path):

    joblib.dump(model, path)


if __name__ == "__main__":

    print("Training pipeline module")