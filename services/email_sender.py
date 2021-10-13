from django.core.mail import mail_managers, send_mail

import logging

logger = logging.getLogger('test_task')


class EmailService:
    def send_contact_email(self, instance):
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
