from django.contrib import admin
from .models import  Appointment, MedicQualification, Patient, Medic, Qualification

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display  = ('patient','medic','date','time','subject','details','created_at','updated_at')
    search_fields = ('patient','medic','date','time')
    list_filter   = ('date' ,'time')

@admin.register(Medic)
class MedicAdmin(admin.ModelAdmin):
    list_display  = ('name', 'last_name'     )
    search_fields = ('name', 'qualifications')
    list_filter   = ('name',                 )

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display  = ('name', 'last_name'     )
    search_fields = ('name',                 )
    list_filter   = ('name',                 )

@admin.register(MedicQualification)
class MedicQualificationAdmin(admin.ModelAdmin):
    list_display  = ('medic', 'qualification' , 'aquired_at')
    search_fields = ('medic', 'qualification' )
    list_filter   = ('medic', 'qualification' )

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display  = ('name',)
    search_fields = ('name',)
    list_filter   = ('name',)