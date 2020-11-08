FROM postgres:latest

WORKDIR /usr/src/app

RUN apt-get -y update
RUN apt-get -y install python3 python3-pip

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY db.py ./
COPY scrape.py ./
COPY ./init.sql /docker-entrypoint-initdb.d/

#CMD ["python3", "./scrape.py"]
