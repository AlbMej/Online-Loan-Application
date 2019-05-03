# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
WORKDIR /code

# Installing OS Dependencies
RUN pip3 install --upgrade pip setuptools

RUN apt-get update && apt-get upgrade -y && apt-get install -y libpq-dev

# Install dependencies
COPY requirements.txt /code/
RUN pip3 install -r /code/requirements.txt

# Copy project
COPY . /code/

# Run
CMD ["python", "loan_app/manage.py", "runserver", "0.0.0.0:8000"]

#Expose server port
EXPOSE 8000