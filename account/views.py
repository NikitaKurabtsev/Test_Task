import json

import requests
from django.shortcuts import render

import account

from .filters import OrderFilter
from .models import User


def index(request):
    data_objects = User.objects.all()
    my_filter = OrderFilter(request.GET, queryset=data_objects)
    data_objects = my_filter.qs
    context = {"data_objects": data_objects, "my_filter": my_filter}
    return render(request, "account/index.html", context)
