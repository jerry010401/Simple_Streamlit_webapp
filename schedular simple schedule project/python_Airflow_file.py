from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depend_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    dag_id="mysql_etl_dag",
    default_args=default_args,
    description="A simple ETL DAG",
    schedule=timedelta(minutes=5),   # updated
    start_date=datetime(2023, 7, 21),
    catchup=False
)

run_etl = BashOperator(
    task_id="run_etl",
    bash_command="bash /home/jerry0104/wrapper_script.sh ",  # update to correct path after space.
    dag=dag
)
