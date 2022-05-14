FROM python:3.8


WORKDIR /eu_reciclo_teste_tecnico

COPY ./app ./app
COPY requirements.txt .

ARG SQLALCHEMY_DATABASE_URI

ENV SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI}

RUN apt-get upgrade -y && apt-get update -y && apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
RUN flask db init

EXPOSE 5000