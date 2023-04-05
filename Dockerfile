FROM arm32v7/python:3.10-bullseye

WORKDIR /code

COPY requirements.txt /code

RUN pip install -r requirements.txt --no-cache-dir

COPY . /code

CMD python3 -u circuit.py
