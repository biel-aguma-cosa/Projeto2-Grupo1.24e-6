from django.contrib import admin
from .models import  Appointment, MedicQualification, Patient, Medic, Qualification

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display  = ('patient','medic','date','time','subject','details','created_at','updated_at')
    search_fields = ('name'   ,'date'        )
    list_filter   = ('name'   ,'date' ,'time')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display  = ('patient','medic','date','time','subject','details','created_at','updated_at')
    search_fields = ('name'   ,'date'        )
    list_filter   = ('name'   ,'date' ,'time')
 