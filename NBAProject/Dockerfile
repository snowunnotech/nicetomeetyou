FROM python:3.7.3
LABEL maintainer gina
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api/
EXPOSE 8000


RUN pip install -r requirements.txt
# RUN python manage.py runserver 0.0.0.0:8000