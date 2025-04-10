from dj_rql.filter_cls import AutoRQLFilterClass

from vehicles.models import Vehicle, VehicleType


class VehicleFilterClass(AutoRQLFilterClass):

    MODEL = Vehicle


class VehicleTypeFilterClass(AutoRQLFilterClass):

    MODEL = VehicleType
