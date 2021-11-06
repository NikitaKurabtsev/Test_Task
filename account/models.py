from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone
import uuid


class User(AbstractUser):
    gender = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


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
