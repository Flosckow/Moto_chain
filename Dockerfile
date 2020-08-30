FROM python:3.8-slim

RUN pip install --no-cache-dir matplotlib pandas

WORKDIR /Desktop/django/moto_shop
пше згыр ву
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt /Desktop/django/moto_shop/requirements.txt

RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN apt-get update && apt-get install netcat -y

COPY . /Desktop/django/moto_shop

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]