# 📊 Churn Prediction Engine for Subscription-Based Products

## Overview

This project implements an **end-to-end churn prediction system** designed for subscription-based products, focusing on **real-world MLOps practices** rather than just model training.

The system combines:

* **Real-time churn prediction** via a FastAPI microservice
* **Automated model retraining** using Apache Airflow
* **Containerized deployment** using Docker

The goal is to demonstrate how machine learning models are **trained, retrained, and served reliably in production-style environments**.

---

## High-Level Architecture

```
Customer Data
   ↓
Model Training (XGBoost)
   ↓
Scheduled Retraining (Airflow DAG)
   ↓
Saved Artifacts (model.pkl, scaler.pkl)
   ↓
FastAPI Service
   ↓
REST API (/predict)
   ↓
Churn Probability Output
```

---

## Project Structure

```
Churn_prediction_project/
├── airflow/
│   └── docker-airflow/
│       ├── dags/
│       │   ├── churn_training_dag.py   # Airflow DAG for retraining
│       │   ├── model.py                # Training & preprocessing logic
│       │   ├── churn.csv               # Training dataset
│       ├── docker-compose-LocalExecutor.yml
│       ├── .env
│       ├── logs/
│       └── plugins/
│
├── fastapi-app/
│   ├── app.py                          # FastAPI application
│   ├── requirements.txt               # API dependencies
│   ├── Dockerfile                     # Containerize FastAPI app
│   ├── sample_input.json              # Example request payload
│   └── README.md
│
├── .gitignore
└── README.md
```

---

## Key Features

* ✅ Predict churn probability for individual customers in real time
* ✅ Automated model retraining using Airflow scheduling
* ✅ Separation of training and serving concerns
* ✅ Dockerized services for reproducibility
* ✅ Clean, modular, and production-oriented code structure

---

## FastAPI Service

### What It Does

* Loads trained model (`model.pkl`) and feature scaler (`scaler.pkl`)
* Exposes a REST endpoint `/predict`
* Accepts JSON input containing customer features
* Returns churn probability or classification

### Run FastAPI Locally

```bash
cd fastapi-app
pip install -r requirements.txt
uvicorn app:app --reload
```

### Test the API

Open your browser and navigate to:

```
http://127.0.0.1:8000/docs
```

Use `sample_input.json` to test predictions via Swagger UI.

---

## Airflow Retraining Pipeline

### What It Does

* Loads historical churn data (`churn.csv`)
* Performs preprocessing and model training (XGBoost)
* Saves artifacts:

  * `model.pkl`
  * `scaler.pkl`
  * `sample_input.json`

### Run Airflow Locally (Docker)

```bash
cd airflow/docker-airflow

docker-compose -f docker-compose-LocalExecutor.yml up airflow-init

docker-compose -f docker-compose-LocalExecutor.yml up
```

### Access Airflow UI

```
http://localhost:8080
```

Login:

* **Username:** airflow
* **Password:** airflow

Steps:

1. Enable DAG `churn_retraining`
2. Trigger the DAG manually
3. Monitor logs for successful retraining

---

## Technologies Used

* Python
* FastAPI
* Apache Airflow
* Docker & Docker Compose
* XGBoost
* scikit-learn
* Pandas & NumPy
* Uvicorn
* REST APIs

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/Sowmya-5G4/Churn-Prediction-Engine-for-Subscription-Based-Products.git
cd Churn-Prediction-Engine-for-Subscription-Based-Products
```

### Start FastAPI

```bash
cd fastapi-app
pip install -r requirements.txt
uvicorn app:app --reload
```

### Start Airflow

```bash
cd airflow/docker-airflow
docker-compose -f docker-compose-LocalExecutor.yml up airflow-init
docker-compose -f docker-compose-LocalExecutor.yml up
```

---

## Notes

* Ensure `churn.csv` is present in the `dags/` directory
* Retrained artifacts are stored inside `dags/`
* Old DAG failures may appear in UI; focus on latest run

---

## What This Project Demonstrates

* End-to-end MLOps pipeline design
* Automated retraining workflows
* Model serving via APIs
* Containerized ML systems
* Separation of training and inference
* Production-style ML engineering practices

---

## Author

Built as a **learning and portfolio project** to demonstrate **practical MLOps system design, model lifecycle management, and API-based ML deployment**.
