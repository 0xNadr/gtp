import sys
import getpass
sys_user = getpass.getuser()
sys.path.append(f"/home/{sys_user}/gtp/backend/")

from datetime import datetime, timedelta
from airflow.decorators import dag, task
from src.misc.airflow_utils import alert_via_webhook

@dag(
    default_args={
        'owner': 'nader',
        'retries': 2,
        'email_on_failure': False,
        'retry_delay': timedelta(minutes=1),
        'on_failure_callback': lambda context: alert_via_webhook(context, user='nader')
    },
    dag_id='raw_starknet',
    description='Load raw tx data from StarkNet',
    tags=['raw', 'near-real-time', 'rpc'],
    start_date=datetime(2023, 9, 1),
    schedule_interval='8/10 * * * *'
)
def adapter_rpc():
    @task(execution_timeout=timedelta(minutes=45))
    def run_starknet():
        from src.adapters.adapter_raw_starknet import AdapterStarknet
        from src.adapters.rpc_funcs.utils import MaxWaitTimeExceededException, get_chain_config
        from src.db_connector import DbConnector

        # Initialize DbConnector
        db_connector = DbConnector()
        
        chain_name = 'starknet'

        active_rpc_configs, batch_size = get_chain_config(db_connector, chain_name)
        print(f"STARKNET_CONFIG={active_rpc_configs}")

        adapter_params = {
            'chain': chain_name,
            'rpc_configs': active_rpc_configs,
        }

        # Initialize AdapterStarknet
        adapter = AdapterStarknet(adapter_params, db_connector)

        # Initial load parameters
        load_params = {
            'block_start': 'auto',
            'batch_size': batch_size,
        }

        try:
            adapter.extract_raw(load_params)
        except MaxWaitTimeExceededException as e:
            print(f"Extraction stopped due to maximum wait time being exceeded: {e}")
            raise e

    run_starknet()
adapter_rpc()