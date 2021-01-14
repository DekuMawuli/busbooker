from django.shortcuts import render, redirect
from .models import Bus, Route, Driver, BusSeat
from django.contrib.auth.models import Group
from django.utils.timezone import datetime


def admin_dashboard(request):
    all_buses = Bus.objects.filter(date_added__date=datetime.now().date())
    bus_on_road = len([bus for bus in all_buses if bus.status == "R"])
    bus_not_on_road = len([bus for bus in all_buses if bus.status == "A"])
    faulty_buses = len([bus for bus in all_buses if bus.status == "F"])
    all_drivers = Driver.objects.filter(date_added__date=datetime.now().date())
    drivers_on_road = len([driver for driver in all_drivers if driver.status == "R"])
    drivers_on_leave = len([driver for driver in all_drivers if driver.status == "L"])
    drivers_not_on_road = len([driver for driver in all_drivers if driver.status == "A"])
    ctx = {
        'buses': all_buses, 'bor': bus_on_road,
        "bnor": bus_not_on_road, 'fb': faulty_buses,
        "drivers": all_drivers, 'dor': drivers_on_road,
        'dol': drivers_on_leave, 'dnor': drivers_not_on_road

    }
    return render(request, "booker/admin-dashboard/admin-dash.html", ctx)


def dashboard(request):
    reg = Group.objects.get(name="Regular")
    if request.user not in reg.user_set.all():
        return admin_dashboard(request)
    else:
        return render(request, "booker/regular/regular-dashboard.html")

