import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle
import os

MODEL_PATH = "outputs/outbreak_model.pkl"

def train_ml_model(outbreak_csv="data/outbreak_data.csv"):
    """
    Train a simple ML model to predict outbreak severity based on region & disease.
    Severity: low=0, medium=1, high=2
    """
    df = pd.read_csv(outbreak_csv)
    df = df.dropna()

    # Encode categorical features
    le_region = LabelEncoder()
    le_disease = LabelEncoder()
    df["region_enc"] = le_region.fit_transform(df["region"])
    df["disease_enc"] = le_disease.fit_transform(df["disease"])
    df["severity_enc"] = df["severity"].map({"low":0, "medium":1, "high":2})

    X = df[["region_enc", "disease_enc"]]
    y = df["severity_enc"]

    model = LogisticRegression(multi_class="multinomial", max_iter=500)
    model.fit(X, y)

    os.makedirs("outputs", exist_ok=True)
    # Save model and encoders
    pickle.dump({"model": model, "le_region": le_region, "le_disease": le_disease}, open(MODEL_PATH, "wb"))
    print("✅ ML model trained and saved.")
    return model, le_region, le_disease

def predict_outbreak_risk(region, disease):
    """
    Predict severity score (0=low,1=medium,2=high) for a disease in a region
    """
    import pickle
    if not os.path.exists(MODEL_PATH):
        train_ml_model()
    
    data = pickle.load(open(MODEL_PATH, "rb"))
    model = data["model"]
    le_region = data["le_region"]
    le_disease = data["le_disease"]

    try:
        region_enc = le_region.transform([region])[0]
    except ValueError:
        region_enc = 0  # unseen region
    try:
        disease_enc = le_disease.transform([disease])[0]
    except ValueError:
        disease_enc = 0  # unseen disease

    pred = model.predict([[region_enc, disease_enc]])[0]
    return int(pred)
