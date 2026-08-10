from django.contrib import admin
from .models import  Appointment, MedicQualification, Patient, Medic, Qualification

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display  = ('patient','medic','date','time','subject','details','created_at','updated_at')
    search_fields = ('date',)
    list_filter   = ('date','time')

@admin.register(Medic)
class MedicAdmin(admin.ModelAdmin):
    list_display  = ('name','last_name')
    search_fields = ('name','last_name')
    list_filter   = ('name',)

@admin.register(MedicQualification)
class MedicQualificationAdmin(admin.ModelAdmin):
    list_display  = ('qualification', 'medic', 'aquired_at')
    search_fields = ('qualification', 'medic',)
    list_filter   = ('qualification',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display  = ('name','last_name')
    search_fields = ('name','last_name')
    list_filter   = ('name',)

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display  = ('name',)
    search_fields = ('name',)
    list_filter   = ('name',)
 
 