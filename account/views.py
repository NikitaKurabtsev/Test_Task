

from django.shortcuts import render


from .filters import GenderFilter
from .models import User


def index(request):
    data_objects = User.objects.all()
    my_filter = GenderFilter(request.GET, queryset=data_objects)
    data_objects = my_filter.qs
    context = {"data_objects": data_objects, "my_filter": my_filter}
    return render(request, "account/index.html", context)
