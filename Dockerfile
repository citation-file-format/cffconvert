FROM python:3.9-alpine

RUN python3 -m pip install cffconvert==2.0.0-alpha.0

WORKDIR /app

ENTRYPOINT ["cffconvert"]
