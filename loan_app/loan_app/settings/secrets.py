SECRET_KEY = 'j7mm6f2qkuw@=d=-cg%4684dp+bkv5t!y%0)klhrfrtfekw_wh'
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'loan_application',
        'USER': 'loaner',
        'PASSWORD': 'postgres',
        'HOST': 'localhost', # set in docker-compose.yml
        'PORT': 5432 # default postgres port
    }
}