#alpine = stripped down version of image, installs only minimal amt of packages
FROM python:3        
 
WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

CMD ["python", "./xray_project_resize.py"]
