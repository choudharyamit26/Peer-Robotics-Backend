from django.db import models

class FlightDetails(models.Model):
    flight_number = models.CharField(max_length=200)
    departure_city = models.CharField(max_length=200)
    departure_time = models.CharField(max_length=200)
    arrival_city = models.CharField(max_length=200)
    arrival_time = models.CharField(max_length=200)