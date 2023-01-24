# syntax=docker/dockerfile:1
FROM python:3.11-bullseye
WORKDIR /code
COPY requirements.txt /code/
COPY requirements-dev.txt /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements-dev.txt
COPY . /code/
RUN pip install -e .