FROM python:3.8-slim

RUN pip install --no-cache-dir matplotlib pandas

WORKDIR /home/daniel/django/moto_shop
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt /home/daniel/django/moto_shop/requirements.txt

RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN apt-get update && apt-get install netcat -y

COPY . /home/daniel/django/moto_shop

