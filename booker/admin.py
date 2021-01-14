from django.contrib import admin
from .models import Bus, Route, Driver, BusSeat
# Register your models here.

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Driver)
admin.site.register(BusSeat)
