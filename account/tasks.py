from .models import Contact

from services.email_sender import _prepare_email

from celery import shared_task


@shared_task
def send_email():  # задача по рассписанию каждую минуту
    contacts = Contact.objects.filter(is_sent=False)
    for contact in contacts:
        _prepare_email(pk=contact.pk)
