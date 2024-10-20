FROM python:3.9-alpine

RUN apk add --no-cache bash curl ca-certificates openssl \
    && apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && apk add --no-cache postgresql-dev \
    && pip install --no-cache-dir requests pandas openpyxl sqlalchemy psycopg2-binary \
    && apk del .build-deps

RUN apk add --no-cache dcron

COPY ./app .

COPY cronjob /etc/cron.d/cronjob

RUN chmod 0644 /etc/cron.d/cronjob

RUN crontab /etc/cron.d/cronjob

RUN touch /var/log/cron.log
