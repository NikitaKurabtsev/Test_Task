from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from contacts.forms import ContactForm

from .filters import GenderFilter
from .models import User


def index(request):
    data_objects = User.objects.all()
    my_filter = GenderFilter(request.GET, queryset=data_objects)
    data_objects = my_filter.qs
    context = {"data_objects": data_objects, "my_filter": my_filter}
    return render(request, "account/index_html.html", context)


def contact_form(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse("Thank you")
    return render(request, "contact/contact_form.html", {"form": form})


@login_required()
def api_list(request):
    context = {}
    return render(request, "account/apis.html", context)