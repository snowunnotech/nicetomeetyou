FROM python:3.6
# To enable logging
ENV PYTHONUNBUFFERED 1
# Create server directory
RUN mkdir -p /srv/project
WORKDIR /srv/project
# Install the server dependencies
COPY requirements.txt /srv/project
RUN pip3 install -r requirements.txt
# Bundle the source
COPY . /srv/project
# Expose port 8000 in the container
EXPOSE 8000