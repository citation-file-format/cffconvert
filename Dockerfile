FROM python:3.9-alpine

RUN python3 -m pip install cffconvert

WORKDIR /app

ENTRYPOINT ["cffconvert"]
