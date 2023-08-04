from app.conf.environ import env

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'postgres',

        'USER': env('PGUSER'),

        'PASSWORD': env('PGPASSWORD'),

        'HOST': env('DB_HOST'),

        'PORT': '5432',

    }

}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'