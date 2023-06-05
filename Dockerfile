FROM amd64/python:3.10-slim

WORKDIR /restaurant_question

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install Django django-cors-headers django-rest-framework Pillow psycopg2-binary

COPY . .

CMD python manage.py runserver 0.0.0.0:8000
