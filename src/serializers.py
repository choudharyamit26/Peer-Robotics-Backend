from rest_framework import serializers
from .models import FlightDetails

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightDetails
        fields = '__all__'