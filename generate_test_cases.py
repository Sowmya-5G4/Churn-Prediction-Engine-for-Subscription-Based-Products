import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import json

# Load and preprocess the data
df = pd.read_csv("churn.csv")
df.drop(columns=['customerID'], inplace=True)
df['Churn'] = LabelEncoder().fit_transform(df['Churn'])

# separate features
X = df.drop(columns=['Churn'])

# one-hot encode categoricals
X = pd.get_dummies(X)

# scale numerical columns
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# save multiple test cases
n_cases = 3  # how many test cases you want
for i in range(n_cases):
    features = [float(x) for x in X.iloc[i].tolist()]
    with open(f"sample_input{i+1}.json", "w") as f:
        json.dump({"features": features}, f)

print(f"Saved {n_cases} test cases: sample_input1.json, sample_input2.json, ..., sample_input{n_cases}.json")
