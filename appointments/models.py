from django.db import models

# Create your models here.
class Medic(models.Model):
    name = models.TextField(max_length=50,verbose_name='Nome')
    last_name = models.TextField(max_length=40,verbose_name='Sobrenome')
    
class Patient(models.Model):
    name      = models.TextField(max_length=20,verbose_name='Nome')
    last_name = models.TextField(max_length=40,verbose_name='Sobrenome')

class Appointment(models.Model):
    medic   = models.ForeignKey(Medic  , models.PROTECT)
    patient = models.ForeignKey(Patient, models.PROTECT)
    date    = models.DateField(verbose_name='Data')