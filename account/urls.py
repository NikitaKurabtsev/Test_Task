from django.urls import include, path

from account.api.router import router

from . import views

app_name = 'account'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('contact/', views.contact_form, name='contact'),
    path('api/', include(router.urls))
]
