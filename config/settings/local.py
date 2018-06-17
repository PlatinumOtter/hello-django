from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='mrdt$g+a#8qp@g+ax5=v^uvicr83el9g$n0utlom9@z(fqnum=')
DEBUG = env.bool('DJANGO_DEBUG', default=True)