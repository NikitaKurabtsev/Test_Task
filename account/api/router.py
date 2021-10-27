from rest_framework import routers

from account.api.views import ContactViewSet
from account.models import Contact

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet, basename=Contact)
urlpatterns = router.urls
