FROM python:3

WORKDIR /src
COPY . /src/

CMD ["python", "listener.py"]
