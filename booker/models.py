from django.db import models
from users.models import CustomUser
from django.utils.timezone import datetime


class Driver(models.Model):
    STATUS = [
        ("A", "Available"),
        ("L", "Leave"),
        ("R", "On Road"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    status = models.CharField(max_length=1, default="A", choices=STATUS)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Route(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    current_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return f"From: {self.current_location} ===> {self.destination}"


class Bus(models.Model):
    STATUS = [
        ("A", "Available"),
        ("F", "Faulty"),
        ("R", "On Road"),
    ]
    TYPES = [
        ("R", "Regular"),
        ("E", "Executive"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    bus_number = models.CharField(max_length=10)
    capacity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default="A", choices=STATUS)
    type = models.CharField(max_length=1, default="R", choices=TYPES)
    seat_price = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)

    class Meta:
        verbose_name_plural = "Buses"

    def __str__(self):
        return f"Bus Number: {self.bus_number}"


class BusSeat(models.Model):
    STATUS = [
        ("B", "Booked"),
        ("U", "Not Booked"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=3)
    passenger_name = models.CharField(max_length=250, default="")
    passenger_phone = models.CharField(max_length=10, default="")
    status = models.CharField(max_length=1, default="U", choices=STATUS)
    time_booked = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Bus Seats"

    def __str__(self):
        return f"{self.bus.bus_number}::: Seat Number: {self.seat_number}"
