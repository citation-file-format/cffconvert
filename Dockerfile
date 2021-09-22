FROM python:3.9-alpine
RUN apk --no-cache add build-base
RUN python3 -m pip install cffconvert==2.0.0
WORKDIR /app
ENTRYPOINT ["cffconvert"]
