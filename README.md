# Online-Loan-Application

## Setup
Make sure to have Python3, virtualenv, and PostgreSQL already pre-installed.

1. Create a virtual environment by running the command `virtualenv env --python=python3.7`
2. Activate the virtual environment by running `. env/bin/activate`
3. Run the following command `sudo apt-get install libpq-dev`
4. Install the dependencies via `pip3 install -r requirements.txt`

### Create Database and User 

We will be using PostgreSQL for our database. Go into the psql terminal (I access it through `psql -U postgres -h localhost postgres`)
Run the following commands:

	postgres=# CREATE USER sample_user WITH PASSWORD 'password';
	CREATE ROLE
	postgres=# CREATE DATABASE sample_database WITH OWNER sample_user;
	CREATE DATABASE

In addition to that, to be able to run the test suite, we will also have to do the following:

	postgres=# ALTER USER loaner CREATEDB;
	ALTER ROLE

Then, in the settings folder, create a secrets.py file in which you will place your secret key and databse credentials. 
They should be in the following form:

	SECRET_KEY = 'sOmE_rAnDoM_50_cHaRaCtEr_StRiNg'

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': '[DB_NAME]',
	        'USER': '[DB_USER]',
	        'PASSWORD': '[USER_PASSWORD]',
	        'HOST': 'localhost',
	        'PORT': 5432 # default postgres port
	    }
	}

### Deploying the application

1. Create the migrations `python3 manage.py makemigrations`
2. Run the migrations `python3 manage.py migrate`
3. Navigate to loan_app and run `python3 manage.py runserver`
4. To deactivate the virtual environment, run the following `deactivate`

### Dockerizing application

I am currently using Window's WSL Ubuntu version Ubuntu 18.04, so I followed this tutorial: 
https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly

*Having trouble configuring Docker to wrok with Django with my Windows 10 WSL setup. A lot of my problems appear to be open issues on GitHub*

## TODO:

  * Implement SMTP Email Backend (Not required but a good addition)
  * Find out why email backend console doesn't work
  * Dockerize application
  * Add to a server (Heroku)