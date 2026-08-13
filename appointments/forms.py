from django import forms
from appointments.models import Qualification

def get_qualifications():
        return [(q.id, q.name) for q in Qualification.objects.all()]
class MedicForm(forms.Form):
    name           = forms.CharField(max_length=50, required=True)
    last_name      = forms.CharField(max_length=40, required=True)
    qualifications = forms.CheckboxSelectMultiple(
        choices = get_qualifications)