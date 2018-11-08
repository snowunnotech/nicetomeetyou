FROM python:3.6.6
LABEL maintainer Muzque
RUN mkdir /docker_api \
 && apt-get update \
 && apt-get install -y vim \
 && pip install --upgrade pip
WORKDIR /docker_api
COPY . /docker_api
RUN pip install -r requirements.txt
