FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y \
gettext
RUN pip install -r requirements.txt
COPY . /code/
