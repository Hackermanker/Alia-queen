FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update -y && apt-get install git gcc python3-dev python3-pip -y

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "FallenRobot"]
