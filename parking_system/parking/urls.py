from rest_framework.routers import DefaultRouter
from parking.views import ParkingRecordViewSet, ParkingSpotViewSet


router = DefaultRouter()
router.register('parking/records', ParkingRecordViewSet)
router.register('parking/spots', ParkingSpotViewSet)

urlpatterns = router.urls
