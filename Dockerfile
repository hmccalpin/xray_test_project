#alpine = stripped down version of image, installs only minimal amt of packages
FROM python:3        
 
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

#COPY . .

CMD ["python", "./xray_project_resize.py"]
