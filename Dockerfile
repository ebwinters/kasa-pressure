FROM arm32v7/python:3.10-bullseye

# RUN apk update && apk add python3-dev \
#                           gcc \
#                           libc-dev \
#                           libffi-dev


WORKDIR /code

COPY requirements.txt /code

RUN pip install -r requirements.txt --no-cache-dir

COPY . /code

CMD python3 circuit.py
