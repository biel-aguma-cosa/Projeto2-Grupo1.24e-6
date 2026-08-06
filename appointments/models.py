from django.db import models

# Create your models here.

class Qualification(models.Model):
    name = models.CharField(max_length=30, verbose_name='Título')
    class Meta:
        ordering     = ['name']
        verbose_name = 'Qualificação'

class Medic(models.Model):
    name           = models.CharField(max_length=50,verbose_name='Nome')
    last_name      = models.TextField(max_length=40,verbose_name='Sobrenome')
    qualifications = models.ManyToManyField(
        Qualification, through='MedicQualification', related_name='medics')
    class Meta:
        ordering     = ['name']
        verbose_name = 'Paciente'

class MedicQualification(models.Model):
    medic         = models.ForeignKey(Medic        , on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)

    aquired_at = models.DateField(verbose_name='Adquirida em')

    
class Patient(models.Model):
    name      = models.TextField(max_length=20,verbose_name='Nome')
    last_name = models.TextField(max_length=40,verbose_name='Sobrenome')
    class Meta:
        ordering     = ['name']
        verbose_name = 'Paciente'

class Appointment(models.Model):
    medic   = models.ForeignKey(Medic  , models.PROTECT, related_name='appointments', verbose_name='Profissional')
    patient = models.ForeignKey(Patient, models.PROTECT, related_name='appointments', verbose_name='Paciente'    )

    subject = models.CharField(verbose_name='Assunto'  , max_length=50            )
    date    = models.DateField(verbose_name='Data'                                )
    time    = models.TimeField(verbose_name='Hora'                                )
    details = models.TextField(verbose_name='Detalhes' , null = True, blank = True)

    created_at = models.DateTimeField(auto_add_now=True, verbose_name='Criada em'    )
    updated_at = models.DateTimeField(auto_now    =True, verbose_name='Atualizada em')
    class Meta:
        ordering = ['date', 'time']
        verbose_name = 'Consulta'