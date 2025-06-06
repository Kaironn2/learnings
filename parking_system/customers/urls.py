from rest_framework.routers import DefaultRouter
from customers.views import CustomerViewSet


router = DefaultRouter()
router.register('customers', CustomerViewSet)

urlpatterns = router.urls
