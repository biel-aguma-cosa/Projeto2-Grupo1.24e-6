from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ConsultaForm
from .models import Consulta


def lista_consultas(request):
    consultas = Consulta.objects.all()
    busca = request.GET.get("busca", "").strip()
    status = request.GET.get("status", "")
    if busca:
        consultas = consultas.filter(
            Q(paciente__icontains=busca)
            | Q(profissional__icontains=busca)
            | Q(especialidade__icontains=busca)
        )
    if status:
        consultas = consultas.filter(status=status)
    contexto = {
        "consultas": consultas,
        "busca": busca,
        "status_selecionado": status,
        "status_choices": Consulta.Status.choices,
        "total": Consulta.objects.count(),
        "agendadas": Consulta.objects.filter(status=Consulta.Status.AGENDADA).count(),
        "confirmadas": Consulta.objects.filter(status=Consulta.Status.CONFIRMADA).count(),
        "realizadas": Consulta.objects.filter(status=Consulta.Status.REALIZADA).count(),
    }
    return render(request, "consultas/lista.html", contexto)


def criar_consulta(request):
    form = ConsultaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Consulta cadastrada com sucesso.")
        return redirect("consultas:lista")
    return render(request, "consultas/form.html", {"form": form, "titulo": "Nova consulta"})


def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    form = ConsultaForm(request.POST or None, instance=consulta)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Consulta atualizada com sucesso.")
        return redirect("consultas:lista")
    return render(request, "consultas/form.html", {"form": form, "titulo": "Editar consulta", "consulta": consulta})


def excluir_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == "POST":
        consulta.delete()
        messages.success(request, "Consulta excluida com sucesso.")
        return redirect("consultas:lista")
    return render(request, "consultas/confirmar_exclusao.html", {"consulta": consulta})
