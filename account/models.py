from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    gender = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
