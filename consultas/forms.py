"""Formulários da aplicação de consultas.

Este módulo define como os dados de uma consulta serão capturados no frontend,
validados pelo Django e salvos no banco. Os campos são transformados em
widgets HTML para melhorar a experiência e manter a consistência dos dados.
"""

from django import forms

from .models import Consulta


class ConsultaForm(forms.ModelForm):
    """Formulário principal para criação e edição de consultas."""

    class Meta:
        # Modelo de dados que será usado no formulário.
        model = Consulta

        # Campos que aparecem na tela para o usuário preencher.
        fields = [
            "paciente", "telefone", "email", "profissional", "especialidade",
            "data", "horario", "status", "observacoes",
        ]

        # Widgets personalizados para melhorar a usabilidade do formulário.
        widgets = {
            "data": forms.DateInput(
                format="%d/%m/%Y",
                attrs={"type": "text", "placeholder": "dd/mm/yyyy"},
            ),
            "horario": forms.TimeInput(
                format="%H:%M",
                attrs={"type": "text", "placeholder": "HH:MM"},
            ),
            "observacoes": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        """Aplica classes CSS e ajustes de entrada para melhor apresentação."""
        super().__init__(*args, **kwargs)

        # Aplica classe Bootstrap/estilo comum a todos os campos do formulário.
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        # O campo de status recebe um estilo específico para select.
        self.fields["status"].widget.attrs["class"] = "form-select"

        # Aceita datas em formato brasileiro e também em formato ISO do Django.
        if "data" in self.fields:
            self.fields["data"].input_formats = ["%d/%m/%Y", "%Y-%m-%d"]

        # Ajusta o campo de horário para aceitar o formato HH:MM.
        if "horario" in self.fields:
            self.fields["horario"].input_formats = ["%H:%M"]
