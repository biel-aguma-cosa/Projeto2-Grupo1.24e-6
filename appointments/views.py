from django.shortcuts import render, redirect
from django.http      import HttpResponse

from . import forms  as app_forms
from . import models as app_model

# Create your views here.
def index(request):
    context = {
        'form' : app_forms.MedicForm()
    }
    return render(request,'index.html',context)

def test(request):
    context = {
            'form' : app_forms.MedicForm()
        }
    if request.method == 'POST':
        form = app_forms.MedicForm(request.POST)
        if form.is_valid():
            medic = app_model.MedicManager.add_medic(
                form.name          ,
                form.last_name     ,
                form.qualifications,
            )

            context['result'] = {
                'name'     : medic.name,
                'lastname' : medic.last_name,
                'quals'    : medic.qualifications,
                'email'    : medic.email,

                'username' : medic.user.username,
                'uemail'    : medic.user.email,
            }
    else:
        context['error'] = 'D:<'
        return render(request,'index.html',context)