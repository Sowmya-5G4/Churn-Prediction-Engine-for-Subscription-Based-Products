📊 Churn Prediction Project
🚀 Overview
This project predicts customer churn for a subscription-based business.
It combines a FastAPI microservice for real-time predictions and an Airflow pipeline for periodic model retraining.

🗂️ Project Structure
graphql
Copy
Edit
project-root/
├── fastapi-app/
│   ├── app.py                # FastAPI server for predictions
│   ├── requirements.txt      # Dependencies for FastAPI
│   ├── Dockerfile            # Containerize FastAPI app
│   ├── sample_input.json     # Example input for prediction
│
├── airflow/
│   └── docker-airflow/
│       ├── dags/
│       │   ├── churn_training_dag.py   # Airflow DAG for retraining
│       │   ├── model.py                # ML training script
│       │   ├── churn.csv               # Training dataset
│       ├── docker-compose-LocalExecutor.yml   # Airflow Docker setup
│       ├── .env                        # Airflow env vars
│       ├── logs/                       # Airflow logs
│       ├── plugins/                    # (optional)
⚡ FastAPI
📄 What it does
✅ Loads trained model & scaler
✅ Exposes /predict API endpoint
✅ Takes a JSON list of features
✅ Returns churn prediction (0 or 1)

🛠️ Run FastAPI locally
bash
Copy
Edit
cd fastapi-app
pip install -r requirements.txt
python app.py
Or with Uvicorn:

bash
Copy
Edit
uvicorn app:app --reload
🌐 Test the API
Open in browser:
http://127.0.0.1:8000/docs
Upload sample_input.json to test.

🛞 Airflow
📄 What it does
✅ Periodically retrains the churn model (model.py) on churn.csv
✅ Saves updated model.pkl, scaler.pkl, and sample_input.json
✅ Runs as a DAG (churn_training_dag.py)

🛠️ Run Airflow locally with Docker
bash
Copy
Edit
cd airflow/docker-airflow

# Initialize Airflow
docker-compose -f docker-compose-LocalExecutor.yml up airflow-init

# Start services
docker-compose -f docker-compose-LocalExecutor.yml up
🌐 Access Airflow UI
http://localhost:8080
Login:

makefile
Copy
Edit
username: airflow
password: airflow
✅ Enable churn_retraining DAG
✅ Trigger it manually
✅ Check logs to verify model retraining

📋 Notes
Trained artifacts (model.pkl, scaler.pkl, sample_input.json) are saved in the dags/ folder after retraining.

Make sure churn.csv exists in the dags/ folder before running the DAG.

The DAG executes model.py using BashOperator.

📦 Technologies Used
🐍 Python

🐳 Docker

⚡ FastAPI

🛞 Apache Airflow

📊 XGBoost, scikit-learn, pandas

