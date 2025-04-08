from rest_framework import serializers

from parking.models import ParkingRecord, ParkingSpot


class ParkingRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingRecord
        fields = '__all__'


class ParkingSpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingSpot
        fields = '__all__'
