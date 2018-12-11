import datetime as dt
import os
from PIL import Image
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
#from airflow.operators.sensors import ExternalTaskSensor


def resize():
    #storing list of image files in dirs variable
    path = "/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/"
    dirs = os.listdir(path)
    
    #creates path for resized image files
    resized_path = path+'resized/'
    if not os.path.exists(resized_path):
        os.makedirs(resized_path)
    
    #ensures no error message when using PIL Image module, which is only compatible with image file formats
    if '.DS_Store' in dirs:
        dirs.remove('.DS_Store')
    
    #create counter to keep track of # of images resized
    resized_counter = 0
    
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
            
            resized_counter += 1
            
    #prints summary statement to dag log
    logging.info("Resized {} x-ray images".format(resized_counter))

def clear_resized_folder():
    #sets path to resized folder and directory of images in resized folder for future looping purposes
    resized_path = "/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/resized/"
    resized_dirs = os.listdir(resized_path)
    
    #create counter to keep track of # images removed from resized folder
    removed_counter = 0
    
    #loops through all images in resized folder and removes one by one 
    for item in resized_dirs:
        os.remove(resized_path+item)
        removed_counter += 1
    
    #prints summary statement to dag log
    logging.info("Removed {} x-ray images from resized folder".format(removed_counter))

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 12, 7),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
    'wait_for_downstream': True,
    'depends_on_past': True
}

with DAG('xray_project_airflow_v02',
         default_args=default_args,
         schedule_interval='0 * * * *',         #runs every hour on the hour
         max_active_runs = 1
        ) as dag:
    
    resize = PythonOperator(task_id='resize',
                            python_callable=resize)
    
    '''wait_for_resize = ExternalTaskSensor(task_id = 'wait_for_resize',
                                         external_dag_id='xray_project_airflow_v02',
                                         external_task_id='resize',
                                        )'''
    
    clear_resized_folder = PythonOperator(task_id='clear_resized_folder',
                                          python_callable=clear_resized_folder,
                                          trigger_rule='all_success')
                                        
    

#clear_resized_folder >> resize
resize.set_downstream(clear_resized_folder)
