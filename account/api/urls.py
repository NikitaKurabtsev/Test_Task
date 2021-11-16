from django.urls import path

from account.api.views import AccountAPI, AccountDetailAPI

app_name = 'api'

urlpatterns = [
    path('accounts/', AccountAPI.as_view(), name='show_accounts'),
    path('accounts/<str:username>/', AccountDetailAPI.as_view(), name='acc_details'),
]
