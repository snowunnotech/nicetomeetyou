FROM python:3.7.3
RUN mkdir /app
WORKDIR /app
COPY . /app


RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000
