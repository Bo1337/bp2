FROM ubuntu:latest
#FROM mhart/alpine-node:base-8

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

RUN mkdir -p /app
#ADD hello-wrld.py /app
COPY . /app/
WORKDIR /app

RUN pip install flask

RUN pip install apscheduler

RUN echo 'Europe/London' >  /etc/timezone

ENTRYPOINT ["python"]

EXPOSE 5080

CMD [ "hello-wrld.py" "/mnt/tst/test.txt" ]
