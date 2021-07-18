import django_filters
from django.db.models import fields

from .models import *
from .models import User


class GenderFilter(django_filters.FilterSet):

    gender = django_filters.ChoiceFilter(
        choices=(("male", 'Male'), ("female", 'Female'),))

    class Meta:
        model = User
        fields = ('gender',)
