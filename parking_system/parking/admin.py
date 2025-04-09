from django.contrib import admin

from parking.models import ParkingRecord, ParkingSpot


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied',]
    search_fields = ['spot_number']
    list_filter = ['is_occupied']


@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_time']
    search_fields = ['vehicle__license_plate', 'parking_spot__spot_number']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parking_spot' and request.resolver_match.url_name.endswith('add'):
            kwargs['queryset'] = ParkingSpot.objects.filter(is_occupied=False)
        elif db_field.name == 'vehicle' and request.resolver_match.url_name.endswith('add'):
            # TODO - filter vehicles that are not already parked
            pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
