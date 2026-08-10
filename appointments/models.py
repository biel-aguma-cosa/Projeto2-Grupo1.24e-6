from django.db import models
import django.contrib.auth.models as auth_models

# Create your models here.

class Qualification(models.Model):
    name = models.CharField(max_length=30, verbose_name='Título')
    class Meta:
        ordering     = ['name']
        verbose_name = 'Qualificação'
        verbose_name_plural = 'Qualificações'

    def __str__(self):
        return f'{self.name}'

class Medic(models.Model):
    name           = models.CharField(max_length=50,verbose_name='Nome')
    last_name      = models.CharField(max_length=40,verbose_name='Sobrenome')
    email          = models.EmailField(null=True, verbose_name='E-Mail')
    qualifications = models.ManyToManyField(
        Qualification, through='MedicQualification', related_name='medics')

    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE)
    class Meta:
        ordering     = ['name']
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
    def __str__(self):
        return f'{self.name} {self.last_name}'

class MedicQualification(models.Model):
    medic         = models.ForeignKey(Medic        , on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)

    aquired_at = models.DateField(verbose_name='Adquirida em')
    class Meta:
        ordering     = ['qualification']
        verbose_name = 'Qualificação do Profissional'
        verbose_name_plural = 'Qualificações dos Profissionais'
    def __str__(self):
            return f'{self.qualification} > {self.medic}'

    
class Patient(models.Model):
    name      = models.CharField (max_length=20,verbose_name='Nome')
    last_name = models.CharField (max_length=40,verbose_name='Sobrenome')

    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE)
    class Meta:
        ordering     = ['name']
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
def __str__(self):
        return f'{self.name} {self.last_name}'

class Appointment(models.Model):
    medic   = models.ForeignKey(Medic  , models.PROTECT, related_name='appointments', verbose_name='Profissional')
    patient = models.ForeignKey(Patient, models.PROTECT, related_name='appointments', verbose_name='Paciente'    )

    subject = models.CharField(verbose_name='Assunto'  , max_length=50            )
    date    = models.DateField(verbose_name='Data'                                )
    time    = models.TimeField(verbose_name='Hora'                                )
    details = models.TextField(verbose_name='Detalhes' , null = True, blank = True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criada em'    )
    updated_at = models.DateTimeField(auto_now    =True, verbose_name='Atualizada em')
    class Meta:
        ordering = ['date', 'time']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
def __str__(self):
        return f'{self.date} {self.last_name}'