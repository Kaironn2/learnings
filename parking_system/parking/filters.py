from dj_rql.filter_cls import AutoRQLFilterClass

from parking.models import ParkingRecord, ParkingSpot


class ParkingRecordFilterClass(AutoRQLFilterClass):

    MODEL = ParkingRecord
    FILTERS = (
        {
            'filter': 'license_plate',
            'source': 'vehicle__license_plate',
        },
    )


class ParkingSpotFilterClass(AutoRQLFilterClass):

    MODEL = ParkingSpot
