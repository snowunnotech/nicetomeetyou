FROM python:3.6.6
LABEL maintainer Muzque
RUN mkdir /nicetomeetyou \
 && apt-get update \
 && apt-get install -y vim \
 && pip install --upgrade pip
WORKDIR /nicetomeetyou
COPY . /nicetomeetyou/
RUN pip install -r requirements.txt
