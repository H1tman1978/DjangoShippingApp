from django.contrib import admin

from .models import Shipment, Address, Package

# Register your models here.
admin.site.register(Shipment)
admin.site.register(Address)
admin.site.register(Package)
