from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    "churn_retraining",
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 0 * * 0",  # every Sunday
    catchup=False,
    tags=["churn"]
) as dag:

    train_model = BashOperator(
        task_id="train_model",
        bash_command="python /usr/local/airflow/dags/model.py"
    )
