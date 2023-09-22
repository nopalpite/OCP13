FROM python:3.10.10

WORKDIR /usr/src/app

ENV PYTHONUNBUFFURED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV SENTRY_DSN $SENTRY_DSN
ENV PORT 8000

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD python manage.py runserver 0.0.0.0:$PORT 
