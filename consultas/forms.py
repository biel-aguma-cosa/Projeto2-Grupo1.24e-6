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
            # display placeholder in dd/mm/yyyy, accept ISO as fallback
            "data": forms.DateInput(format="%d/%m/%Y", attrs={"type": "text", "placeholder": "dd/mm/yyyy"}),
            "horario": forms.TimeInput(format="%H:%M", attrs={"type": "text", "placeholder": "HH:MM"}),
            "observacoes": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields["status"].widget.attrs["class"] = "form-select"
        # accept both dd/mm/YYYY (user-facing) and ISO yyyy-mm-dd (browsers/backfills)
        if 'data' in self.fields:
            self.fields['data'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']
        if 'horario' in self.fields:
            self.fields['horario'].input_formats = ['%H:%M']
