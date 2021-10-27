from celery import shared_task

from services.email_sender import EmailService

from .models import Contact

email_service = EmailService()


@shared_task
def send_email():
    contacts = Contact.objects.filter(is_sent=False)
    for contact in contacts:
        send_email_by_contact.delay(pk=contact.pk)


@shared_task
def send_email_by_contact(pk):
    email_service.send_contact_email(pk=pk)
