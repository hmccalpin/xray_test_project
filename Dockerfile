FROM python:alpine        #alpine = stripped down version of image, installs only minimal amt of packages

ADD xray_project_resize.py

RUN

CMD ["python", "./my_script.py"]
