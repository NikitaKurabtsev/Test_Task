from celery import shared_task

from .signals import post_save_contact


@shared_task
def email_sender():
    post_save_contact()
