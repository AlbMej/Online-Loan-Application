# Online-Loan-Application

## Setup

1. Create a virtual environment by running the command `virtualenv env --python=python3.7`
2. Run the following command `sudo apt-get install libpq-dev`
3. Install the dependencies via `pip install -r requirements.txt`

### Create Database and User 

We will be using PostgreSQL for our database. Run the following commands inside the psql terminal (I access it through `psql -U postgres -h localhost postgres`)

	postgres=# CREATE USER sample_user WITH PASSWORD 'password';
	CREATE ROLE
	postgres=# CREATE DATABASE sample_database WITH OWNER sample_user;
	CREATE DATABASE

Then, you will create a secrets.py file in which you will place your secret key and databse credentials. 
They should be in the following form 

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

1. Create the migrations `python manage.py makemigrations`
2. Run the migrations `python manage.py migrate`
3. Navigate to loan_app and run `python manage.py runserver`
2. Activate the virtual environment by running `. env/bin/activate`
3. Run the following command to install the dependencies `pip install -r requirements.txt`
4. Navigate to loan_app and run `python manage.py runserver`
5. To deactivate the virtual environment, run the following `deactivate`

### Dockerizing application

I am currently using Window's WSL Ubuntu version Ubuntu 18.04, so I followed this tutorial: 
https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly

## TODO:

  * Implement SMTP Email Backend (Not required but a good addition)
  * Find out why email backend console doesn't work
  * Add test cases
  * Dockerize application
  * Add to a server (Heroku)