# Base image
FROM python:3.11.7

WORKDIR /app

RUN apt-get update -y
RUN apt-get install tk -y

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
