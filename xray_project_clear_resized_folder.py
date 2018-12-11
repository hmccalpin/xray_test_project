import os

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
