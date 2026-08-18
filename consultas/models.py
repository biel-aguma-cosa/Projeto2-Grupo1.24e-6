"""Modelos do sistema de agendamento de consultas.

Este módulo representa a entidade principal da aplicação: uma consulta médica.
Cada registro guarda dados do paciente, profissional, horário, status e demais
informações essenciais para a gestão da agenda.
"""

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q


class Consulta(models.Model):
    """Representa uma consulta agendada, confirmada, realizada ou cancelada."""

    class Status(models.TextChoices):
        """Enum de status possíveis para cada consulta."""

        AGENDADA = "agendada", "Agendada"
        CONFIRMADA = "confirmada", "Confirmada"
        REALIZADA = "realizada", "Realizada"
        CANCELADA = "cancelada", "Cancelada"

    # Dados do paciente que busca o atendimento.
    paciente = models.CharField("paciente", max_length=120)
    telefone = models.CharField("telefone", max_length=20, blank=True)
    email = models.EmailField("e-mail", blank=True)

    # Dados do profissional responsável pelo atendimento.
    profissional = models.CharField("profissional", max_length=120)
    especialidade = models.CharField("especialidade", max_length=100)

    # Data e horário previstos para a consulta.
    data = models.DateField("data")
    horario = models.TimeField("horario")

    # Status da consulta, com valores controlados pelo TextChoices.
    status = models.CharField(
        "status",
        max_length=12,
        choices=Status.choices,
        default=Status.AGENDADA,
    )

    # Observações complementares sobre a consulta.
    observacoes = models.TextField("observacoes", blank=True)

    # Metadados de auditoria: quando foi criada e quando foi atualizada.
    criado_em = models.DateTimeField("criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        # Ordena a agenda por data e horário para facilitar a visualização.
        ordering = ["data", "horario"]
        verbose_name = "consulta"
        verbose_name_plural = "consultas"

        # Garante que o mesmo profissional não tenha dois atendimentos no mesmo
        # horário, exceto quando a consulta está cancelada.
        constraints = [
            models.UniqueConstraint(
                fields=["profissional", "data", "horario"],
                condition=~Q(status="cancelada"),
                name="consulta_profissional_data_horario_unicos",
            )
        ]

    def clean(self):
        """Valida conflitos de agenda antes de salvar a consulta."""
        if self.data and self.horario and self.status != self.Status.CANCELADA:
            conflito = (
                Consulta.objects.filter(
                    profissional=self.profissional,
                    data=self.data,
                    horario=self.horario,
                )
                .exclude(pk=self.pk)
                .exclude(status=self.Status.CANCELADA)
                .exists()
            )
            if conflito:
                raise ValidationError("Este profissional ja possui uma consulta neste horario.")

    def __str__(self):
        """Texto amigável usado em listagens e administração."""
        return f"{self.paciente} - {self.data:%d/%m/%Y} {self.horario:%H:%M}"
