from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    gender = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="ім'я")
    email = models.EmailField(max_length=50, verbose_name="пошта")
    comment = models.TextField(max_length=150, verbose_name="коментар")
    file = models.FileField(
        upload_to='',
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc"])],
        verbose_name="файл",
        help_text="завантажте pdf або doc документ"
    )

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.comment[:15]}"
