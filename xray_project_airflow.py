import datetime as dt

import os, random
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import csv

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def get_rand_img():
    #pull random image from file of sample images
    rand_img = random.choice(os.listdir('/Users/haleymccalpin/Desktop/XRayProject/sample_images'))                       
    return(rand_img)
 
    
    #get_diagnosis(rand_img)
    get_diagnosis(rand_img)


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 12, 4),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('airflow_tutorial_v01',
         default_args=default_args,
         schedule_interval='0/5 * * * *',         #runs every 5 min
         ) as dag:

    print_hello = BashOperator(task_id='print_hello',
                               bash_command='echo "hello"')
    sleep = BashOperator(task_id='sleep',
                         bash_command='sleep 5')
    print_world = PythonOperator(task_id='print_world',
                                 python_callable=print_world)


print_hello >> sleep >> print_world
