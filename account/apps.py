from django.apps import AppConfig

# from account.signals import post_save_contact


class ApiViewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    def ready(self):
        from django.db.models.signals import post_save
        from account.models import Contact
        from account.signals import post_save_contact

        post_save.connect(post_save_contact, sender=Contact)
