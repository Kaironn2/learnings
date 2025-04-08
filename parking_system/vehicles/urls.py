from rest_framework.routers import DefaultRouter
from vehicles.views import VehicleTypeViewSet, VehicleViewSet


router = DefaultRouter()
router.register('vehicles/types', VehicleTypeViewSet)
router.register('vehicles', VehicleViewSet)

urlpatterns = router.urls
