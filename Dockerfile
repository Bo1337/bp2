FROM python:3

ADD hello-wrld.py /
RUN pip install flask

CMD [ "python", "./hello-wrld.py" ]

