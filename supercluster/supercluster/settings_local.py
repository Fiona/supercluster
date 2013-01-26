DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Make sure this is filled with something!!!!
SECRET_KEY = '$vt6pxel1no&amp;9bedx@xpn20-$wv=j2achj=)$yals@)t0+up&amp;4'

ADMINS = (
    ('Admin', 'admin@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'supercluster',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/London'
