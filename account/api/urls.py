from django.urls import path

from .views import AccountAPI, AccountDetailAPI, GetContactAPI, GetNewContactAPI

app_name = 'api_account'
urlpatterns = [
    path('accounts/', AccountAPI.as_view(), name='show_accounts'),
    path('accounts/<str:username>/', AccountDetailAPI.as_view(), name='acc_details'),
    path('contacts/', GetContactAPI.as_view(), name='get_contacts'),
    path('get_new_contacts/', GetNewContactAPI.as_view(), name='get_new_contacts')
]
