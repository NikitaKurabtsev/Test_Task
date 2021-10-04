from django.core.mail import mail_managers, send_mail

from account.models import Contact

import logging


logfile = 'email_errors.log'

log = logging.getLogger("my_log")
log.setLevel(logging.INFO)
FH = logging.FileHandler(logfile)
basic_formater = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
FH.setFormatter(basic_formater)
log.addHandler(FH)


def _prepare_email(pk):
    instance = Contact.objects.get(pk=pk)
    try:
        subject = f'Message from {instance.name}'
        mail_managers(subject, instance.comment)
        send_mail(
            subject="Fitelio",
            message="дякуємо, ваше резюме було прийнято",
            from_email="От комп...",
            recipient_list=[instance.email],
            fail_silently=True
        )
        instance.is_sent = True
        instance.save()
        log.info("email sent successfully")
    except Exception as error:
        log.error(error)
