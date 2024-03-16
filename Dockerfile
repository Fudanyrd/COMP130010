# syntax=docker/dockerfile:1
FROM python:3.11-alpine

WORKDIR /usr/src

# install necessary packages
COPY requirements.txt requirements.txt
# citation: I solved this problem using infor on 
# <https://stackoverflow.com/questions/76533384/docker-alpine-build-fails-on-mysqlclient-installation-with-error-exception-can>
RUN apk add --no-cache --virtual build-deps gcc musl-dev pkgconf mariadb-dev && \
    apk add --no-cache mariadb-connector-c-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-deps
# RUN pip3 install -r requirements.txt
# citation: solved ModuleNotFoundException with the help of
# <https://blog.csdn.net/weixin_73778478/article/details/127822215>
RUN pip install mysql-connector-python

# copy necessary files into venv
COPY . .
# RUN python manage.py collectstatic --no-input
# RUN python manage.py makemigrations
# RUN sleep 10
# RUN python manage.py migrate

# start the application
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# to build the application, run:
# ```
# docker-compose up --build
# ```