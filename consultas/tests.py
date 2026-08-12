from datetime import date, time

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from .models import Consulta


class ConsultaFlowTests(TestCase):
    def setUp(self):
        self.consulta = Consulta.objects.create(
            paciente="Ana Souza",
            profissional="Dra. Marina Lima",
            especialidade="Cardiologia",
            data=date(2026, 8, 12),
            horario=time(9, 30),
        )

    def test_lista_exibe_consulta_e_busca_filtra(self):
        response = self.client.get(reverse("consultas:lista"), {"busca": "Ana"})
        self.assertContains(response, "Ana Souza")
        self.assertContains(response, "Cardiologia")

    def test_criar_consulta(self):
        response = self.client.post(reverse("consultas:criar"), {
            "paciente": "Bruno Costa",
            "telefone": "11999999999",
            "email": "bruno@example.com",
            "profissional": "Dra. Carla Alves",
            "especialidade": "Dermatologia",
            "data": "2026-08-13",
            "horario": "14:00",
            "status": "agendada",
            "observacoes": "Primeira consulta",
        })
        self.assertRedirects(response, reverse("consultas:lista"))
        self.assertTrue(Consulta.objects.filter(paciente="Bruno Costa").exists())

    def test_impede_conflito_de_profissional(self):
        conflito = Consulta(
            paciente="Carlos Mendes",
            profissional=self.consulta.profissional,
            especialidade="Cardiologia",
            data=self.consulta.data,
            horario=self.consulta.horario,
        )
        with self.assertRaisesMessage(ValidationError, "Este profissional ja possui uma consulta neste horario."):
            conflito.full_clean()

    def test_excluir_consulta(self):
        response = self.client.post(reverse("consultas:excluir", args=[self.consulta.pk]))
        self.assertRedirects(response, reverse("consultas:lista"))
        self.assertFalse(Consulta.objects.filter(pk=self.consulta.pk).exists())