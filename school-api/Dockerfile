FROM python:3.9.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./school-api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .