from airflow.operators.sql import SQLCheckOperator

SQLCheckOperator(
    task_id="yellow_trip data_row_quality_check",
    sql="row_quality_yellow_trip data_check.sql",
    params={"pickup_datetime": "2021-01-01"},
)