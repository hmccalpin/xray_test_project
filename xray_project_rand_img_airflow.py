import datetime as dt

import os, random, sys
from PIL import Image
import matplotlib.pyplot as plt


import matplotlib.image as mpimg
import csv
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def pull_rand_img():
    #pull random image from file of sample images
    rand_img = random.choice(os.listdir('/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images'))                       
    return(rand_img)
 
def get_dx(**context):
    #grabs rand_img from previous task
    current_rand_img_ID = context['task_instance'].xcom_pull(task_ids='pull_rand_img')
    #open sample_labels.csv and find random image diagnosis
    with open('/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/sample_labels.csv') as csvfile:
        sample_labels = csv.reader(csvfile)
         
        for row in sample_labels: 
            if row[0] == current_rand_img_ID:                
                #print image ID, visual image, and corresponding diagnosis
                x_ray = Image.open('/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/{}'.format(current_rand_img_ID))
                return('image ID:', current_rand_img_ID, '\ndiagnosis:', row[1], '\nimage:', plt.imshow(x_ray))
                return(plt.imshow(x_ray))


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 12, 4),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
    'wait_for_downstream': True,
    'depends_on_past': True
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



pull_rand_img.set_downstream(get_dx)

