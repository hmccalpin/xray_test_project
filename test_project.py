import numpy as np # linear algebra
import pandas as pd #data processing

import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import csv

''' 
Read through each x-ray image file name
'''
def main():
    for root, dirs, files in os.walk('/Users/haleymccalpin/Desktop/XRayProject/sample_images'):
        for img_name in files:
            print('image:', img_name)
            get_diagnosis(img_name)
    
'''
Cross-reference x-ray image file name with sample_labels.csv and output image file name with corresponding dx
'''
def get_diagnosis(image):
    with open('/Users/haleymccalpin/Desktop/XRayProject/sample_labels.csv') as csvfile:
        sample_labels = csv.reader(csvfile)
        for row in sample_labels: 
            if row[0] == image:
                print('image:', image, '--', row[1])
main()
