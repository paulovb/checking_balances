FROM python:3.6.6

WORKDIR /app
ADD requirements.txt /app
RUN pip install --no-cache-dir -q -r requirements.txt

ADD . /app

CMD gunicorn project.wsgi -b 0.0.0.0:5000