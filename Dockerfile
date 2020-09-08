FROM python:3.8-slim


WORKDIR /home/daniel/django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y
RUN pip install --upgrade pip

COPY requirements.txt /home/daniel/django/requirements.txt

RUN pip install -r requirements.txt
RUN pip install gunicorn


COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/home/daniel/django/entrypoint.sh"]
