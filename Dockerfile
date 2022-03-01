FROM python:3.8

WORKDIR /app
COPY ./app /app
RUN pip install -r requirements.txt
EXPOSE 8000

