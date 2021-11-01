from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Contact, Record, User

admin.site.register(User, UserAdmin)

admin.site.register(Contact)

admin.site.register(Record)