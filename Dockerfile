FROM python:3.7-slim

WORKDIR /usr/src/app

COPY main.py .

CMD [ "python", "./main.py" ]
