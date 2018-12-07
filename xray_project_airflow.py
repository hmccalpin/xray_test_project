import datetime as dt

import os, random, sys
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
    current_rand_img_ID = context['task_instance'].xcom_pull(task_ids='pull_rand_img')
    #open sample_labels.csv and find random image diagnosis
    with open('/Users/haleymccalpin/Desktop/XRayProject/sample_labels.csv') as csvfile:
        sample_labels = csv.reader(csvfile)
         
        for row in sample_labels: 
            if row[0] == current_rand_img_ID:                
                #print image ID, visual image, and corresponding diagnosis
                x_ray = Image.open('/Users/haleymccalpin/Desktop/XRayProject/sample_images/{}'.format(current_rand_img_ID))
                return('image ID:', current_rand_img_ID, '\ndiagnosis:', row[1], '\nimage:', plt.imshow(x_ray))
                return(plt.imshow(x_ray))

        
def resize():
    #storing list of image files in dirs variable
    path = "/Users/haleymccalpin/Desktop/XRayProject/sample_images/"
    dirs = os.listdir(path)
    
    #creates path for resized image files
    resized_path = path+'resized/'
    if not os.path.exists(resized_path):
        os.makedirs(resized_path)
    
    #ensures no error message when using PIL Image module, which is only compatible with image file formats
    if '.DS_Store' in dirs:
        dirs.remove('.DS_Store')
    
    #loop through all image files in sample_images folder
    for item in dirs:
        
        #ensures only regular files are being opened 
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            
            #removes .png from original image directory so that we can append 'resized'  
            og_image_path, ext = os.path.splitext(path+item)
            
            #resizes image to 200 pixels (width, height)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            
            #splits image directory into everything leading up to final image ID
            resized_image_directory, resized_imageID = os.path.split(og_image_path)
            
            #saves resized image .png into resized/ folder 
            imResize.save(resized_path + resized_imageID +' resized.png', 'PNG', quality=90)

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
    
    resize = PythonOperator(task_id='resize',
                            python_callable=resize)
    

'''with DAG('xray_project_airflow_v02',
         default_args=default_args,
         schedule_interval='0/5 * * * *',
        ) as dag:
'''
    
    

get_dx >> pull_rand_img >> resize
