import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save


def _upload_file_cv(obj, file: str):
    now = timezone.now().astimezone(timezone.get_current_timezone()).strftime("%Y/%m/%d")
    _file_struc = file.split(".")
    if len(_file_struc) > 1:
        _ext = _file_struc[-1]
        _file = "_".join(_file_struc[0: -1])
        file_name = f"{_file}-{uuid.uuid4()}.{_ext}"
    else:
        file_name = f"{uuid.uuid4()}"
    return f"cv/{obj.name}/{now}/{file_name}"


class User(AbstractUser):
    gender = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ім'я")
    email = models.EmailField(max_length=50, verbose_name="Пошта")
    comment = models.TextField(max_length=150, verbose_name="Коментар", blank=True, default="")
    is_sent = models.BooleanField(default=False)
    file = models.FileField(
        upload_to=_upload_file_cv,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc"])],
        verbose_name="Файл",
        help_text="Завантажте pdf або doc документ"
    )

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.comment[:15]}"


@receiver(post_save, sender=Contact)
def post_save_contact_2(sender, instance, created, **kwargs):
    pass
