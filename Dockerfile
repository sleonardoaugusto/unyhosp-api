# pull official base image
FROM python:3

# set work directory
WORKDIR /usr/src/unyhosp-api/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/unyhosp-api/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/unyhosp-api