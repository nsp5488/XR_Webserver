FROM python:3

WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update && apt-get install poppler-utils apache2 apache2-dev -y
COPY requirements.txt requirements.txt
RUN pip install uwsgi
RUN pip install --no-cache-dir -r requirements.txt

# Setup the environment to what the application expects
COPY . /usr/src/app
COPY templates /usr/src/app/templates
EXPOSE  8000
CMD ["uwsgi", "--http", "0.0.0.0:8000", "--master", "-w", "wsgi:app"]


