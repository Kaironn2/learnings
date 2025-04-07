from rest_framework import viewsets

from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
