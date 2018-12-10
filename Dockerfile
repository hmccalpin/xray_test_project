#alpine = stripped down version of image, installs only minimal amt of packages
FROM python:3        
 
ADD xray_project_resize.py /
#WORKDIR xray_test_project_github/

RUN pip install -r requirements.txt

CMD ["python", "./xray_project_resize.py"]
