from django.contrib import admin

from .models import Shipment, Address, Package, Part, Machine

# Register your models here.
admin.site.register(Shipment)
admin.site.register(Address)
admin.site.register(Package)
admin.site.register(Part)
admin.site.register(Machine)
