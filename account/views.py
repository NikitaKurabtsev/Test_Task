import json

import requests
from django.shortcuts import render

import account

from .filters import OrderFilter
from .models import User


def index(request):
    users_query = User.objects.all()
    url = "https://randomuser.me/api/?results=100"
    data = requests.get(url).json()["results"]
    while len(users_query) < 100:
        for user_data in data:
            user = User.objects.get_or_create(
                username=user_data.get("login", {}).get("username", ""),
                password=user_data.get("login", {}).get("password", ""),
                first_name=user_data.get("name", {}).get("first", ""),
                last_name=user_data.get("name", {}).get("last", ""),
                gender=user_data.get("gender", ""),
            )
    data_objects = User.objects.all()
    my_filter = OrderFilter(request.GET, queryset=data_objects)
    data_objects = my_filter.qs
    context = {"data_objects": data_objects, "my_filter": my_filter}
    return render(request, "account/index.html", context)
