from rest_framework import routers

from contacts.api.views import ContactViewSet
from contacts.models import Contact

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contacts')

urlpatterns = router.urls
