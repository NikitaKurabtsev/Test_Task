from django.http import HttpResponse
from django.shortcuts import render

from contacts.forms import ContactForm


def contact_form(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse("Thank you")
    return render(request, "contact/contact_form.html", {"form": form})
