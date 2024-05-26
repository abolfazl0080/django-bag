FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /app/
