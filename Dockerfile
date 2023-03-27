FROM python:3.10-alpine

WORKDIR /code

COPY requirements.txt /code

RUN pip install -r requirements.txt --no-cache-dir

COPY . /code

CMD python3 -u control_lights.py
