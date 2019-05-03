SECRET_KEY = 'j7mm6f2qkuw@=d=-cg%4684dp+bkv5t!y%0)klhrfrtfekw_wh'
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

# settings.py

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost', # set in docker-compose.yml
#         'PORT': 5432 # default postgres port
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

DATABASE_URL = "postgres://vswhajcyqxynyv:b9061a4d6df50e47f8284a6459a1a18603c1072bac417451fbe0a7b81cefe719@ec2-174-129-10-235.compute-1.amazonaws.com:5432/d7h1dd5os1cnj"