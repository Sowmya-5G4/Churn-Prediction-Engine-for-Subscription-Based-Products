import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from xgboost import XGBClassifier
import joblib
import json

#  Load data
df = pd.read_csv("churn.csv")

#Drop irrelevant column
df.drop(columns=['customerID'], inplace=True)

# Encode target
df['Churn'] = LabelEncoder().fit_transform(df['Churn'])

#  Features & Target
X = df.drop(columns=['Churn'])
y = df['Churn']

#  One-hot encode categorical columns
X = pd.get_dummies(X)

#  Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f" Number of features: {X.shape[1]}")

#  Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Train model
model = XGBClassifier()
model.fit(X_train, y_train)

# Save model & scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')


sample = [float(x) for x in X.iloc[0].tolist()]  # convert numpy to native float
with open("sample_input.json", "w") as f:
    json.dump({"features": sample}, f)

print("✅ Model, scaler, and sample_input.json saved successfully!")
