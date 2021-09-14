from django.shortcuts import render
from django.core.mail import mail_managers, send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse


from .filters import GenderFilter
from .models import User
from account.forms import ContactForm


def index(request):
    data_objects = User.objects.all()
    my_filter = GenderFilter(request.GET, queryset=data_objects)
    data_objects = my_filter.qs
    context = {"data_objects": data_objects, "my_filter": my_filter}
    return render(request, "account/index.html", context)


def contact_form(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        subject = f'Message from {form.cleaned_data["name"]}'
        message = form.cleaned_data["comment"]
        sender = form.cleaned_data["email"]
        manager_email = settings.MANAGERS
        form.save()
        try:
            mail_managers(subject, message)
            send_mail(
                subject = "Fitelio",
                message = "дякуємо, ваше резюме було прийнято",
                from_email = manager_email,
                recipient_list = [sender]
            )
        except BadHeaderError:
            return HttpResponse("Invalid header")
        return HttpResponse("Thank you")
    return render(request, "contact/contact_form.html", {"form": form})
