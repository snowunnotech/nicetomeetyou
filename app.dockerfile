FROM python:3.6.0

COPY ./app /app
COPY ./requirements /requirements
COPY ./conf.d/uwsgi.ini /uwsgi/uwsgi.ini
# install service required module
RUN pip install -r /requirements/requirements.txt

# execute the command when the container run
CMD uwsgi --ini /uwsgi/uwsgi.ini

