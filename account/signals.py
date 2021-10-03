from django.core.mail import mail_managers, send_mail

from .models import Contact
import logging


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


# # def post_save_contact(sender, instance, created, **kwargs):

#     try:
#         subject = f'Message from {instance.name}'
#         mail_managers(subject, instance.comment)
#         send_mail(
#             subject="Fitelio",
#             message="дякуємо, ваше резюме було прийнято",
#             from_email="От комп...",
#             recipient_list=instance.email
#         )
#     except Exception as error:
#         log.error(error)


def _prepare_email(pk):
    # непосредственная отправка писем
    instance = Contact.objects.get(pk=pk)
    try:
        subject = f'Message from {instance.name}'
        mail_managers(subject, instance.comment)
        send_mail(
            subject="Fitelio",
            message="дякуємо, ваше резюме було прийнято",
            from_email="От комп...",
            recipient_list=(instance.email,)
        )
        instance.is_sent = True
        instance.save()
    except Exception as error:
        log.error(error)


def post_save_contact(sender, instance, created, **kwargs):  # задача по рассписанию каждую минуту
    contacts = Contact.objects.filter(is_sent=False)
    for contact in contacts:
        _prepare_email(pk=contact.pk)
