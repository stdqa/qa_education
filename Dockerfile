FROM python:3.8-alpine

#ARG run_env=db_tests
#ENV env $run_env


LABEL "education"="automation"

WORKDIR ./usr/lessons

VOLUME /allureResults

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip3 install -r requirements.txt


COPY . .

CMD pytest -s -v tests/* --alluredir=allureResults