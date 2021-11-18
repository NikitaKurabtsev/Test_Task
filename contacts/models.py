import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from account.models import User


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


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(max_length=50, verbose_name="Email")
    comment = models.TextField(max_length=150, verbose_name="Comment", blank=True, default="")
    is_sent = models.BooleanField(default=False, verbose_name="feedback is sent")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="create date")
    file = models.FileField(
        upload_to=_upload_file_cv,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc"])],
        verbose_name="File",
        help_text="load pdf or doc document"
    )

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.comment[:15]}"


class Record(models.Model):
    """Table for recording user refresh api contacts"""
    record_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="record_user",
                                    verbose_name="користувач")
    update = models.DateTimeField(auto_now=True, verbose_name="last query date")

    def __str__(self) -> str:
        return f"{self.record_user} {self.update}"
