import sys
import getpass
sys_user = getpass.getuser()
sys.path.append(f"/home/{sys_user}/gtp/backend/")

from datetime import datetime,timedelta
from airflow.decorators import dag, task 
from src.misc.airflow_utils import alert_via_webhook

@dag(
    default_args={
        'owner' : 'mseidl',
        'retries' : 2,
        'email_on_failure': False,
        'retry_delay' : timedelta(minutes=5),
        'on_failure_callback': alert_via_webhook
    },
    dag_id='raw_imx',
    description='Load raw data on withdrawals, deposits, trades, orders_filled, transfers, mints.',
    tags=['raw', 'near-real-time'],
    start_date=datetime(2023,4,24),
    schedule_interval='*/17 * * * *'
)

def etl():
    @task(execution_timeout=timedelta(minutes=45))
    def run_imx():
        from src.db_connector import DbConnector
        from src.adapters.adapter_raw_imx import AdapterRawImx

        adapter_params = {
            'load_types' : ['withdrawals', 'deposits', 'transfers', 'mints'],
            'forced_refresh' : 'no',
        }
       # initialize adapter
        db_connector = DbConnector()
        ad = AdapterRawImx(adapter_params, db_connector)
        # extract & load incremmentally
        ad.extract_raw()

    run_imx()
etl()