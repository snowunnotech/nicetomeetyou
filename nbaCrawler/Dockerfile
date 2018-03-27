FROM python:3.6.4
LABEL maintainer Jerry
ENV PYTHONUNBUFFERED 1
RUN mkdir /nbaCrawler
WORKDIR /nbaCrawler
COPY . /nbaCrawler/
RUN pip install -r requirements.txt
