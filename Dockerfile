FROM python:3.6.6
LABEL maintainer Muzque
RUN mkdir /nicetomeetyou
WORKDIR /nicetomeetyou
COPY . /nicetomeetyou/
RUN pip install -r requirements.txt
