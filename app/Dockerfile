From python:3.7.7

RUN pip3 install --upgrade pip
RUN pip install bottle
RUN pip install uwsgi

COPY todo.py /opt/app
COPY uwsgi.ini /opt/app