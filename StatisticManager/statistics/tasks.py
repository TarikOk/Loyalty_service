from celery import shared_task
from services import new_entry
from views import control_balance


@shared_task(bind=True)    
def entry():
    new_entry()


@shared_task(bind=True)
def test_balance():
    control_balance()