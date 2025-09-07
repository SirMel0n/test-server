# Dockerfile, Image, Container

FROM python:3.9
COPY . /test-app
WORKDIR /test-app
RUN pip install requests

CMD python server.py
