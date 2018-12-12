import datetime as dt
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 12, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
    'wait_for_downstream': True,
    'depends_on_past': True
}

with DAG('xray_project_airflow-docker',
         default_args=default_args,
         schedule_interval='0/5 * * * *',         #runs every 5 min
         max_active_runs = 1
         ) as dag:

    build_resize_container = BashOperator(task_id='build_resize_container',
                                          bash_command='cd X-Ray-Resize && docker build -t resize',
                                          dag=dag)
                                          
    run_resize_container = BashOperator(task_id='run_resize_container',
                                        bash_command='docker run resize',
                                        trigger_rule='all_success',
                                        dag=dag)
    
    stop_resize_container = BashOperator(task_id='stop_resize_container',
                                         bash_command='docker stop resize',
                                         trigger_rule='all_success',
                                         dag=dag)
                        
build_resize_container >> run_resize_container >> stop_resize_container
