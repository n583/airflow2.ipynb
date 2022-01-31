import datetime as dt

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2021, 1, 29),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}