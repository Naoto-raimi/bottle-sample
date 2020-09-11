FROM tiangolo/uwsgi-nginx:python3.7

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

ADD nginx.conf /etc/nginx/conf.d/

RUN mkdir -p /opt/uwsgi
COPY uwsgi.ini /opt/uwsgi/uwsgi.ini
ENV UWSGI_INI /opt/uwesgi/uwesgi.ini

WORKDIR /var/www/app