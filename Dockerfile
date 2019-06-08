FROM python:3

ENV PYTHONUNBUFFERED 1
ENV LANG en_US.UTF-8
ENV TZ Asia/Taipei


RUN mkdir /code

WORKDIR /code

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    cron

# set up project python env
COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock
RUN pip3 install pipenv && pipenv install --system --deploy

# Django post setup script
RUN mkdir -p /etc/init.d
COPY docker/init.sh /etc/init.d/init.sh
RUN chmod +x /etc/init.d/init.sh


# Copy hello-cron file to the cron.d directory
COPY core/scrapy-cron /etc/cron.d/scrapy-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/scrapy-cron

# Apply cron job
RUN crontab /etc/cron.d/scrapy-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . /code/
