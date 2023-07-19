FROM python:3.18-alpine
RUN apk --no-cache add build-base
RUN python3 -m pip install cffconvert==3.0.0a0
WORKDIR /app
ENTRYPOINT ["cffconvert"]
