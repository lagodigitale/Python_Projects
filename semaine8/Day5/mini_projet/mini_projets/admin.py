
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Vehicule)
admin.site.register(TypeVehicule)
admin.site.register(TailleVehicule)
admin.site.register(TarifLocation)
admin.site.register(Location)