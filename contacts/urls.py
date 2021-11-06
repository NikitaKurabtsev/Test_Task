from django.urls import path, include
from .views import contact_form


app_name = 'contact'

urlpatterns = [
    path('contact/', contact_form, name='contact_form'),
    path('api/', include('contacts.api.urls'))
]
