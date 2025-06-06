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
    dag_id='metrics_l2beat',
    description='Load onchain TVL.',
    tags=['metrics', 'daily'],
    start_date=datetime(2023,4,24),
    schedule='50 03 * * *'
)

def etl():
    @task()
    def run_tvs():
        from src.db_connector import DbConnector
        from src.adapters.adapter_l2beat import AdapterL2Beat

        adapter_params = {}
        load_params = {
            'origin_keys' : None,
            'load_type' : 'tvs',
        }

       # initialize adapter
        db_connector = DbConnector()
        ad = AdapterL2Beat(adapter_params, db_connector)
        # extract
        df = ad.extract(load_params)
        # load
        ad.load(df)

    @task()
    def run_stages():
        from src.db_connector import DbConnector
        from src.adapters.adapter_l2beat import AdapterL2Beat

        adapter_params = {}
        load_params = {
            'origin_keys' : None,
            'load_type' : 'stages',
        }

       # initialize adapter
        db_connector = DbConnector()
        ad = AdapterL2Beat(adapter_params, db_connector)
        # extract
        df = ad.extract(load_params)
        # load
        ad.load(df)

    @task()
    def run_sys_table():
        from src.db_connector import DbConnector
        from src.adapters.adapter_l2beat import AdapterL2Beat

        adapter_params = {}
        load_params = {
            'origin_keys' : None,
            'load_type' : 'sys_l2beat',
        }

       # initialize adapter
        db_connector = DbConnector()
        ad = AdapterL2Beat(adapter_params, db_connector)
        # extract
        df = ad.extract(load_params)
        # load
        ad.load(df)
    
    run_tvs()
    run_stages()
    run_sys_table()
etl()