from .models import Contact

from services.email_sender import EmailService

from celery import shared_task

email_service = EmailService()


@shared_task
def send_email():
    contacts = Contact.objects.filter(is_sent=False)
    for contact in contacts:
        email_service.send_contact_email(instance=contact)
