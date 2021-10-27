from django.http import HttpResponse
from django.shortcuts import render

from account.forms import ContactForm

from .filters import GenderFilter
from .models import User


def index(request):
    data_objects = User.objects.all()
    my_filter = GenderFilter(request.GET, queryset=data_objects)
    data_objects = my_filter.qs
    context = {"data_objects": data_objects, "my_filter": my_filter}
    return render(request, "account/index.html", context)


def contact_form(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse("Thank you")
    return render(request, "contact/contact_form.html", {"form": form})
