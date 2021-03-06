from portfolio.settings.base import *

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'portfolio/static')

]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'https://my-portfolio-jay.herokuapp.com/static/'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = "F:/Projects/web apps/junk/secondProject/portfolio - project/media"
MEDIA_URL = 'https://my-portfolio-jay.herokuapp.com/media/'

DEBUG = False
ALLOWED_HOSTS = ['my-portfolio-jay.herokuapp.com']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

###################### production setting ################################



SECRET_KEY = os.environ.get('SECRET_KEY', 'SOME+RANDOM+KEY(z9+3vnm(jb0u@&w68t#5_e8s9-lbfhv-')  


import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True