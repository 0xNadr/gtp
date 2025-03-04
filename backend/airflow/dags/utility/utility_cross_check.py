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
    dag_id='utility_cross_check',
    description='Load txcount data from explorers and check against our database. Send discord message if there is a discrepancy.',
    tags=['utility', 'daily'],
    start_date=datetime(2023,12,9),
    schedule='30 06 * * *'
)

def etl():
    @task()
    def run_explorers():
        from src.db_connector import DbConnector
        from src.adapters.adapter_cross_check import AdapterCrossCheck

        adapter_params = {}

        load_params = {
            'origin_keys' : None,
        }

       # initialize adapter
        db_connector = DbConnector()
        ad = AdapterCrossCheck(adapter_params, db_connector)
        # extract
        df = ad.extract(load_params)
        # load
        ad.load(df)

        ## cross-check and send Discord message
        ad.cross_check()

        ## cross-check Celestia
        ad.cross_check_celestia()
    
    run_explorers()
etl()