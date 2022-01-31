from airflow.operators.bash import BashOperator
from datetime import timedelta
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.sql import SQLThresholdCheckOperator, SQLIntervalCheckOperator
from airflow.providers.mysql.operators.mysql

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def ispalindrome():
    s = [1, 2, 3, 4]
    s = s[::-1]
    return s


default_args = {'owner': 'airflow',
                'retry_delay': timedelta(minutes=5),
                'start_date': datetime(2021, 1, 30),
                }

with DAG(
        dag_id='tutorial',
        default_args=default_args,
        description='A simple tutorial DAG',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 30),
        catchup=False,
        tags=['example'],
) as dag:
    t1 = BashOperator(
        task_id="check file",
        bash_command="if[ -e  airflow_ex.csv]",
        retries=2,
        retry_delay=timedelta(seconds=15)

    )
    t2 = PythonOperator(
        task_id="python_job",
        python_callable=ispalindrome()

    )
    t3 = MySqlOperator(
         task_id= "sql_job"
        sql= 
    )

    SQLThresholdCheckOperator(
        task_id="check_threshold",
        sql="SELECT MAX(passenger_count)",
        min_threshold=1,
        max_threshold=8
    )

    SQLIntervalCheckOperator(
        task_id="check_interval_data",
        days_back=1,
        date_filter_column="upload_date",
        metrics_threshold={"AVG(trip_distance)": 1.5}
    )