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
# citation: solved ModuleNotFoundException with the help of
# <https://blog.csdn.net/weixin_73778478/article/details/127822215>
RUN pip install mysql-connector-python

# copy necessary files into venv
COPY . .
# to build the application, run:
# ```
# docker-compose up --build
# ```