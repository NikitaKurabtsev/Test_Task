import logging

from django.core.mail import mail_managers, send_mail

from account.models import Contact

logger = logging.getLogger('test_task')


class EmailService:
    def send_contact_email(self, pk):
        instance = Contact.objects.get(pk=pk)
        try:
            try:
                subject = f'Message from {instance.name}'
                mail_managers(subject, instance.comment)
                logger.info('email to managers sent successfully')
            except Exception as error:
                logger.error(error)
            try:
                subject = f'Message from {instance.name}'
                mail_managers(subject, instance.comment)
                send_mail(
                    subject='Fitelio',
                    message='дякуємо, ваше резюме було прийнято',
                    from_email='От комп...',
                    recipient_list=[instance.email],
                    fail_silently=True
                )
                instance.is_sent = True
                instance.save()
                logger.info('email sent successfully')
                return self
            except Exception as error:
                logger.error(error)
            logger.info('email to client and managers sent successfully')
        except Exception as error:
            logger.error(error)
