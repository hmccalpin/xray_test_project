#alpine = stripped down version of image, installs only minimal amt of packages
FROM python:3        
 
COPY . /xray_test_project_github
WORKDIR /xray_test_project_github

RUN pip install -r requirements.txt

#COPY . .

CMD ["python", "./xray_project_resize.py"]
