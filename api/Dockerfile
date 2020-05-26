FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PORT 80

COPY . /opt/api
COPY wait-for-it.sh /opt/api/
WORKDIR /opt/api

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
