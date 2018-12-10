#alpine = stripped down version of image, installs only minimal amt of packages
FROM python:alpine        
 
ADD xray_project_resize.py

RUN pip install requests

CMD ["python", "./xray_project_resize.py"]
