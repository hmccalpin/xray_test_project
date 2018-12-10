#alpine = stripped down version of image, installs only minimal amt of packages
FROM python:3        
 
#moves application into  container image
COPY ./app

#set working directory
WORKDIR /app

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Pillow
#COPY . .

CMD ["python", "./xray_project_resize.py"]
