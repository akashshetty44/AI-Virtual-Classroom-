import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# ---------------------------------------
# Configuration
# ---------------------------------------
DATASET = "prediction/student_dataset.csv"
MODEL_FILE = "prediction/student_model.pkl"


# ---------------------------------------
# Train Model
# ---------------------------------------
def train_model():

    if not os.path.exists(DATASET):
        print("Dataset not found!")
        return

    # Load dataset
    data = pd.read_csv(DATASET)

    # Input Features
    X = data[
        [
            "attendance",
            "quiz_score",
            "assignment_score"
        ]
    ]

    # Output Label
    y = data["performance"]

    # Split Dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Train Model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Accuracy
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("\n==============================")
    print("Model Trained Successfully")
    print("==============================")
    print(f"Accuracy : {accuracy * 100:.2f}%")

    # Save Model
    joblib.dump(model, MODEL_FILE)

    print(f"Model saved as: {MODEL_FILE}")


# ---------------------------------------
# Main
# ---------------------------------------
if __name__ == "__main__":
    train_model()
