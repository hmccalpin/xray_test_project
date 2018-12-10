FROM python:3.6        #alpine = stripped down version of image, installs only minimal amt of packages
 
ADD xray_project_resize.py

RUN pip install requests

CMD ["python", "./xray_project_resize.py"]
