import datetime as dt
import airflow
from airflow import DAG
from datetime import timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.sql import SQLCheckOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.providers.sqlite import operators


# Example of creating a task that calls a common CREATE TABLE sql command.
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

from airflow1 import dag

create_table_sqlite_task = SqliteOperator(
    task_id='create_table_sqlite',
    sql=r"""
    CREATE TABLE Customers (
        customer_id INT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    );
    """,
    dag=dag,

)

drop_table_mysql_task = MySqlOperator(
    task_id='create_table_mysql', sql=r"""DROP TABLE table_name;""", dag=dag)
from MySQLdb import _mysql
db=_mysql.connect()

db=_mysql.connect(host="localhost",user="jobbed",
                  passwd="moon pie",db="things")
db.query("""SELECT spam, eggs, sausage FROM breakfast
         WHERE price < 5""")
r=db.store_result()
# ...or...
r=db.use_result()
SQLCheckOperator(
    task_id="yellow_tripdata_row_quality_check",
    sql="row_quality_yellow_tripdata_check.sql",
    params={"pickup_datetime": "2021-01-01"},
)









