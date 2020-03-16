import os
from celery import Celery
 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stat_app.settings')
 
app = Celery('stat_app')

app.config_from_object('django.conf:settings')
 
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)