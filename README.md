📊 Churn Prediction Engine for Subscription-Based Products
🚀 Overview
This project is a Churn Prediction Engine designed for subscription-based products.
It consists of two main components:

🔷 A FastAPI microservice for real-time churn predictions.

🔷 An Airflow pipeline for periodic model retraining.

It helps businesses predict customer churn and proactively improve customer retention.

🗂️ Project Structure

Churn_prediction_project/
├── airflow/
│   └── docker-airflow/
│       ├── dags/
│       │   ├── churn_training_dag.py      # Airflow DAG: retrain pipeline
│       │   ├── model.py                   # ML training script
│       │   ├── churn.csv                  # Training dataset
│       ├── docker-compose-LocalExecutor.yml   # Airflow Docker setup
│       ├── .env
│       ├── logs/                          # Airflow logs (optional)
│       ├── plugins/                       # (optional)
│
├── fastapi-app/
│   ├── app.py                     # FastAPI service
│   ├── requirements.txt           # Python dependencies
│   ├── Dockerfile                 # Containerize FastAPI app
│   ├── sample_input.json          # Example prediction input
│
├── README.md                      # Project documentation
├── .gitignore
✨ Features
✅ Predict churn probability for individual customers in real time.
✅ Schedule periodic retraining on updated data.
✅ Scalable and containerized with Docker.
✅ Clear and modular code with Airflow orchestration and FastAPI serving.

⚡ FastAPI Service
📄 What it does
Loads the trained churn prediction model (model.pkl) and scaler.

Exposes a REST endpoint /predict to serve predictions.

Takes a JSON array of customer features and returns churn probabilities or labels.

🛠️ Run FastAPI Locally

cd fastapi-app
pip install -r requirements.txt
python app.py
Or with Uvicorn:

bash
Copy
Edit
uvicorn app:app --reload
🌐 Test the API
Go to:
➡️ http://127.0.0.1:8000/docs
You can upload sample_input.json here to test predictions.

🛞 Airflow Retraining Pipeline
📄 What it does
Loads churn.csv dataset.

Preprocesses & trains a churn prediction model.

Outputs:

model.pkl: trained model

scaler.pkl: feature scaler

sample_input.json: sample test input

🛠️ Run Airflow Locally with Docker

cd airflow/docker-airflow

# Initialize Airflow database
docker-compose -f docker-compose-LocalExecutor.yml up airflow-init

# Start Airflow services
docker-compose -f docker-compose-LocalExecutor.yml up
🌐 Access Airflow UI
➡️ http://localhost:8080
Login:

username: airflow
password: airflow
✅ Enable the DAG: churn_retraining
✅ Trigger it manually from UI.
✅ Check logs to confirm retraining was successful.

📦 Technologies Used
🐍 Python

⚡ FastAPI

🛞 Apache Airflow

🐳 Docker

📊 scikit-learn, XGBoost, Pandas

🚀 Setup & Deployment
🔷 Clone the repository

git clone https://github.com/Sowmya-5G4/Churn-Prediction-Engine-for-Subscription-Based-Products.git
cd Churn-Prediction-Engine-for-Subscription-Based-Products
🔷 Setup FastAPI

cd fastapi-app
pip install -r requirements.txt
uvicorn app:app --reload
🔷 Setup Airflow

cd airflow/docker-airflow
docker-compose -f docker-compose-LocalExecutor.yml up airflow-init
docker-compose -f docker-compose-LocalExecutor.yml up
📋 Notes
✅ Make sure churn.csv is present in the dags/ folder.
✅ Outputs of retraining (model.pkl, scaler.pkl, sample_input.json) are saved in dags/.
✅ Old task failures remain in Airflow UI — focus on latest run results.



