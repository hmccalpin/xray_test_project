import os
from PIL import Image

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

