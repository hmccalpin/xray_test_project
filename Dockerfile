#alpine = stripped down version of image, installs only minimal amt of packages
FROM python:3        
 
WORKDIR /xray_test_project_github
#COPY requirements.txt ./

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Pillow
#COPY . .

CMD ["python", "./xray_project_resize.py"]
