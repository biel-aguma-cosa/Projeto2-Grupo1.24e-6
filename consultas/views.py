"""Views do app de consultas.

Estas funções controlam a lógica de apresentação e interação da agenda:
- listagem e filtros;
- cadastro de nova consulta;
- edição de registros existentes;
- exclusão com confirmação.
"""

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ConsultaForm
from .models import Consulta


def lista_consultas(request):
    """Exibe a agenda com busca, filtros por status e ordenação."""
    # Busca todas as consultas do banco como base para os filtros.
    consultas = Consulta.objects.all()

    # Captura o termo de busca digitado pelo usuário na página.
    busca = request.GET.get("busca", "").strip()
    order = request.GET.get("order", "")

    # Aplica busca por paciente, profissional ou especialidade.
    if busca:
        consultas = consultas.filter(
            Q(paciente__icontains=busca)
            | Q(profissional__icontains=busca)
            | Q(especialidade__icontains=busca)
        )

    # Coleta os status selecionados no filtro do formulário.
    statuses = request.GET.getlist("statuses")
    if not statuses:
        raw = request.GET.get("statuses", "")
        if raw:
            statuses = [s for s in raw.split(",") if s]

    if statuses:
        consultas = consultas.filter(status__in=statuses)

    # Campos permitidos para ordenação na lista da agenda.
    valid_fields = {
        "paciente": ["paciente"],
        "profissional": ["profissional"],
        "especialidade": ["especialidade"],
        "data": ["data", "horario"],
        "status": ["status"],
    }

    # Aplica a ordenação informada pela interface.
    if order:
        desc = order.startswith("-")
        key = order[1:] if desc else order
        if key in valid_fields:
            fields = valid_fields[key]
            if desc:
                fields = ["-" + f for f in fields]
            consultas = consultas.order_by(*fields)

    # Monta o contexto para renderização do template com estatísticas e filtros.
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

    # Mantém os parâmetros atuais da URL ao criar links de ordenação.
    params = request.GET.copy()
    if "order" in params:
        del params["order"]
    contexto["base_qs"] = params.urlencode()

    # Gera os links de ordenação para cada campo da tabela.
    sort_links = {}
    for key in valid_fields.keys():
        if order == key:
            target = "-" + key
            arrow = "▲"
        elif order == "-" + key:
            target = key
            arrow = "▼"
        else:
            target = key
            arrow = ""

        href = "?"
        if contexto["base_qs"]:
            href += contexto["base_qs"] + "&"
        href += "order=" + target
        sort_links[key] = {"href": href, "arrow": arrow, "target": target}

    contexto["sort_links"] = sort_links
    return render(request, "consultas/lista.html", contexto)


def criar_consulta(request):
    """Cria uma nova consulta usando o formulário de cadastro."""
    form = ConsultaForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Consulta cadastrada com sucesso.")
        return redirect("consultas:lista")

    return render(request, "consultas/form.html", {"form": form, "titulo": "Nova consulta"})


def editar_consulta(request, pk):
    """Edita uma consulta já existente com base no identificador da instância."""
    consulta = get_object_or_404(Consulta, pk=pk)
    form = ConsultaForm(request.POST or None, instance=consulta)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Consulta atualizada com sucesso.")
        return redirect("consultas:lista")

    return render(
        request,
        "consultas/form.html",
        {"form": form, "titulo": "Editar consulta", "consulta": consulta},
    )


def excluir_consulta(request, pk):
    """Exclui uma consulta após confirmação do usuário."""
    consulta = get_object_or_404(Consulta, pk=pk)

    if request.method == "POST":
        consulta.delete()
        messages.success(request, "Consulta excluida com sucesso.")
        return redirect("consultas:lista")

    return render(request, "consultas/confirmar_exclusao.html", {"consulta": consulta})
