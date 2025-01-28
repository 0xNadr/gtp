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
        'retries' : 5,
        'email_on_failure': False,
        'retry_delay' : timedelta(minutes=10),
        'on_failure_callback': alert_via_webhook
    },
    dag_id='metrics_coingecko',
    description='Load price, volume, and market_cap from coingecko API for all tracked tokens.',
    tags=['metrics', 'daily'],
    start_date=datetime(2023,4,24),
    schedule='05 02 * * *'
)

def etl():
    @task()
    def run_market_chart():
        from src.db_connector import DbConnector
        from src.adapters.adapter_coingecko import AdapterCoingecko

        adapter_params = {}
        load_params = {
            'load_type' : 'project',
            'metric_keys' : ['price', 'volume', 'market_cap'],
            'origin_keys' : None, # could also be a list
            'days' : 'auto', # auto, max, or a number (as string)
            'vs_currencies' : ['usd', 'eth']
        }

        # initialize adapter
        db_connector = DbConnector()
        ad = AdapterCoingecko(adapter_params, db_connector)
        # extract
        df = ad.extract(load_params)
        # load
        ad.load(df)

    @task()
    def run_direct():
        from src.db_connector import DbConnector
        from src.adapters.adapter_coingecko import AdapterCoingecko
        
        adapter_params = {}
        load_params = {
            'load_type' : 'direct',
            'metric_keys' : ['price', 'volume', 'market_cap'],
            'coingecko_ids' : ['glo-dollar'],
            'days' : 'auto', # auto, max, or a number (as string)
            'vs_currencies' : ['usd', 'eth']
        }

        # initialize adapter
        db_connector = DbConnector()
        ad = AdapterCoingecko(adapter_params, db_connector)
        # extract
        df = ad.extract(load_params)
        # load
        ad.load(df)
    
    run_market_chart()
    run_direct()
etl()