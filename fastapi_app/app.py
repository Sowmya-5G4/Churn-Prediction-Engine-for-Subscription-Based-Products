from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model & scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

class FeaturesInput(BaseModel):
    features: list

@app.post("/predict")
def predict(data: FeaturesInput):
    X = np.array(data.features).reshape(1, -1)
    X_scaled = scaler.transform(X)
    pred = model.predict(X_scaled)[0]
    return {"churn": int(pred)}
