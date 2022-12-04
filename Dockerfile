FROM python:3.8

WORKDIR /app
COPY . /app

RUN addgroup server
RUN useradd --user-group -ms /bin/bash app

ENV PYTHONUNBUFFERED 1
ENV APP_DIR=/app

RUN pip install --disable-pip-version-check -r /app/requirements.txt
RUN chown -R app:app $APP_DIR
USER app