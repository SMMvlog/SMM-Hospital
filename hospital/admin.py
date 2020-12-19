from django.contrib import admin
from .models import Docter,Patient,Appointment
# Register your models here.

admin.site.register(Docter)
admin.site.register(Patient)
admin.site.register(Appointment)
