# import logging
# from django.core.mail import mail_managers, send_mail
# from .models import Contact


# log = logging.getLogger(__name__)
# log.setLevel(logging.INFO)


# def post_save_contact(sender, instance, created, **kwargs):

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


# def task2(pk):
#     # непосредственная отправка писем
#     instance = Contact.objects.get(pk)
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


# def task1():  # задача по рассписанию каждую минуту
#     contacts = Contact.objects.filter()
#     for contact in contacts:
#         task2.delay(pk=contact.pk)
