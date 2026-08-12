from django import forms

from .models import Consulta


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = [
            "paciente", "telefone", "email", "profissional", "especialidade",
            "data", "horario", "status", "observacoes",
        ]
        widgets = {
            "data": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "horario": forms.TimeInput(format="%H:%M", attrs={"type": "time"}),
            "observacoes": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields["status"].widget.attrs["class"] = "form-select"
