from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ConsultaForm
from .models import Consulta


def lista_consultas(request):
    consultas = Consulta.objects.all()
    busca = request.GET.get("busca", "").strip()
    order = request.GET.get('order', '')
    if busca:
        consultas = consultas.filter(
            Q(paciente__icontains=busca)
            | Q(profissional__icontains=busca)
            | Q(especialidade__icontains=busca)
        )
    # single 'status' parameter removed; use multi-status 'statuses' instead
    # support multi-status filtering via ?statuses=agendada&statuses=confirmada or comma-separated
    statuses = request.GET.getlist('statuses')
    if not statuses:
        raw = request.GET.get('statuses', '')
        if raw:
            statuses = [s for s in raw.split(',') if s]
    if statuses:
        consultas = consultas.filter(status__in=statuses)
    # Ordering
    valid_fields = {
        'paciente': ['paciente'],
        'profissional': ['profissional'],
        'especialidade': ['especialidade'],
        'data': ['data', 'horario'],
        'status': ['status'],
    }
    if order:
        desc = order.startswith('-')
        key = order[1:] if desc else order
        if key in valid_fields:
            fields = valid_fields[key]
            if desc:
                fields = ['-' + f for f in fields]
            consultas = consultas.order_by(*fields)
    contexto = {
        "consultas": consultas,
        "busca": busca,
        "status_choices": Consulta.Status.choices,
        "total": Consulta.objects.count(),
        "agendadas": Consulta.objects.filter(status=Consulta.Status.AGENDADA).count(),
        "confirmadas": Consulta.objects.filter(status=Consulta.Status.CONFIRMADA).count(),
        "realizadas": Consulta.objects.filter(status=Consulta.Status.REALIZADA).count(),
        "order": order,
    }
    # build base querystring without order
    params = request.GET.copy()
    if 'order' in params:
        del params['order']
    contexto['base_qs'] = params.urlencode()
    # prepare sort links and indicators
    sort_links = {}
    for key in valid_fields.keys():
        if order == key:
            target = '-' + key
            arrow = '▲'
        elif order == '-' + key:
            target = key
            arrow = '▼'
        else:
            target = key
            arrow = ''
        href = '?'
        if contexto['base_qs']:
            href += contexto['base_qs'] + '&'
        href += 'order=' + target
        sort_links[key] = {'href': href, 'arrow': arrow, 'target': target}
    contexto['sort_links'] = sort_links
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
