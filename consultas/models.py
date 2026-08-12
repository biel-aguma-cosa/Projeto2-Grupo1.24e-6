from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q


class Consulta(models.Model):
    class Status(models.TextChoices):
        AGENDADA = "agendada", "Agendada"
        CONFIRMADA = "confirmada", "Confirmada"
        REALIZADA = "realizada", "Realizada"
        CANCELADA = "cancelada", "Cancelada"

    paciente = models.CharField("paciente", max_length=120)
    telefone = models.CharField("telefone", max_length=20, blank=True)
    email = models.EmailField("e-mail", blank=True)
    profissional = models.CharField("profissional", max_length=120)
    especialidade = models.CharField("especialidade", max_length=100)
    data = models.DateField("data")
    horario = models.TimeField("horario")
    status = models.CharField("status", max_length=12, choices=Status.choices, default=Status.AGENDADA)
    observacoes = models.TextField("observacoes", blank=True)
    criado_em = models.DateTimeField("criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        ordering = ["data", "horario"]
        verbose_name = "consulta"
        verbose_name_plural = "consultas"
        constraints = [
            models.UniqueConstraint(
                fields=["profissional", "data", "horario"],
                condition=~Q(status="cancelada"),
                name="consulta_profissional_data_horario_unicos",
            )
        ]

    def clean(self):
        if self.data and self.horario and self.status != self.Status.CANCELADA:
            conflito = Consulta.objects.filter(
                profissional=self.profissional,
                data=self.data,
                horario=self.horario,
            ).exclude(pk=self.pk).exclude(status=self.Status.CANCELADA).exists()
            if conflito:
                raise ValidationError("Este profissional ja possui uma consulta neste horario.")

    def __str__(self):
        return f"{self.paciente} - {self.data:%d/%m/%Y} {self.horario:%H:%M}"
