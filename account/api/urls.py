from django.urls import path

from .views import AccountAPI

app_name = 'api_account'
urlpatterns = [
    path('accounts/', AccountAPI.as_view(), name='show_accounts'),
]

