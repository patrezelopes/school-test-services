FROM python:3.7 AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./django-core/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
