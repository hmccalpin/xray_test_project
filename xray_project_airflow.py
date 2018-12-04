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


def pull_rand_img():
    #pull random image from file of sample images
    rand_img = random.choice(os.listdir('/Users/haleymccalpin/Desktop/XRayProject/sample_images'))                       
    return(rand_img)
 
def get_dx(**context):
    #grabs rand_img from previous task
    current_rand_img = context['task_instance'].xcom_pull(task_ids='pull_rand_img')['rand_img']
    #open sample_labels.csv and find random image diagnosis
    with open('/Users/haleymccalpin/Desktop/XRayProject/sample_labels.csv') as csvfile:
        sample_labels = csv.reader(csvfile)
         
        for row in sample_labels: 
            if row[0] == image_ID:                
                #print image ID, visual image, and corresponding diagnosis
                x_ray = Image.open('/Users/haleymccalpin/Desktop/XRayProject/sample_images/{}'.format(image_ID))
                print('image ID:', image_ID, '\ndiagnosis:', row[1], '\nimage:', plt.imshow(x_ray))    
 


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 12, 4),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('xray_project_airflow_v01',
         default_args=default_args,
         schedule_interval='0/5 * * * *',         #runs every 5 min
         ) as dag:

    pull_rand_img = PythonOperator(task_id='pull_rand_img',
                                   python_callable=pull_rand_img)
    get_dx = PythonOperator(task_id='get_dx',
                            python_callable=get_dx,
                            provide_context = True)

get_dx >> pull_rand_img
