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

Make sure to download Docker Desktop. 
The Dockerfile and docker-compose.yml includes the necessary to dockerize this application. Make sure to remove any environment folders before dockerizing the application (e.g. /env/)
To use the database within the container, you must change the DATABASES variable to:

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': 'postgres',
	        'USER': 'postgres',
	        'HOST': 'db',
	        'PORT': 5432,
	    }
	}

Now, in Powershell, run `docker-compose up --build` and wait as it builds the container. 
When the log shows "database system is ready to accept connections", open up a new Powershell window in the root of the project directory.

Run the following commands:

	docker-compose run --rm web python loan_app/manage.py makemigrations --settings=loan_app.settings.settings
	docker-compose run --rm web python loan_app/manage.py migrate --settings=loan_app.settings.settings
	docker-compose run --rm -p 8000:8000 web python loan_app/manage.py runserver 0.0.0.0:8000

Viola! The project is now running through a container :)
Access it through http://127.0.0.1:8000/

### Set up project on a Heroku server

Make sure to have the Heroku CLI pre installed. In my Ubuntu 18.04 terminal, I used `curl https://cli-assets.heroku.com/install-ubuntu.sh | sh`

1. Login to Heroku: `heroku login`
2. Install the Heroku container registry plugin for the CLI: `heroku plugins:install @heroku-cli/plugin-container-registry`
3. Login to the registry: `heroku container:login`
4. Create a Heroku app:

	You can do by just running `heroku create` and it will randomly generate an app name for you
	Or you can dp something like `heroku create albmej-loan-application`

5. Then, push your image: `heroku container:push web --app albmej-loan-application`

Unfortunately steps 6 and 7 do not work with my Windows setup. Running through a lot of headaches trying to get it to work. 

6. At this point the next step would be to release the image: `heroku container:push web --app albmej-loan-application`
7. Then `heroku open --app albmej-loan-application` to check out the live app

## TODO:

  * Implement SMTP Email Backend (Not required but a good addition)
  * Find out why email backend console doesn't work
  * Add to a server (Heroku)