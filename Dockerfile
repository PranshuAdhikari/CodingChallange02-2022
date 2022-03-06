# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

#WORKDIR /usr/app/src
COPY . ./

CMD [ "python", "main.py" ]


