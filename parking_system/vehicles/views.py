from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets

from core.permissions import IsVehicleOrRecordOwner
from vehicles.filters import VehicleFilterClass, VehicleTypeFilterClass
from vehicles.models import Vehicle, VehicleType
from vehicles.serializers import VehicleSerializer, VehicleTypeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    rql_filter_class = VehicleFilterClass
    permission_classes = [DjangoModelPermissions, IsVehicleOrRecordOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    rql_filter_class = VehicleTypeFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]
