import numpy as np # linear algebra
import pandas as pd #data processing

import os, random
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import csv

def main():
    #pull random image from file of sample images
    rand_img = random.choice(os.listdir('/Users/haleymccalpin/Desktop/XRayProject/sample_images'))                       
    
    #get_diagnosis(rand_img)
    get_diagnosis(rand_img)
                             
def get_diagnosis(image_ID):
    
    #open sample_labels.csv and find random image diagnosis
    with open('/Users/haleymccalpin/Desktop/XRayProject/sample_labels.csv') as csvfile:
        sample_labels = csv.reader(csvfile)
         
        for row in sample_labels: 
            if row[0] == image_ID:                
                #print image ID, visual image, and corresponding diagnosis
                x_ray = Image.open('/Users/haleymccalpin/Desktop/XRayProject/sample_images/{}'.format(image_ID))
                print('image ID:', image_ID, '\ndiagnosis:', row[1], '\nimage:', plt.imshow(x_ray))

                
main()
