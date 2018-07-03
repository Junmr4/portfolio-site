from portfolio.settings.base import *
ALLOWED_HOSTS = []
DEBUG = True

STATICFILES_DIRS = [

    #"F:/Projects/web apps/junk/secondProject/portfolio - project/static"
    os.path.join(BASE_DIR, 'portfolio/static')

]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_ROOT = "F:/Projects/web apps/junk/secondProject/portfolio - project/media"
MEDIA_URL = '/media/'

