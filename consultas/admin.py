"""Configuração da administração do Django para o app de consultas."""

from django.contrib import admin

from .models import Consulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    """Personaliza a interface administrativa da entidade Consulta.

    A classe controla como os registros aparecem na área administrativa,
    incluindo colunas exibidas, filtros, busca e ordenação.
    """

    # Campos mostrados na listagem principal da administração.
    list_display = ("paciente", "profissional", "especialidade", "data", "horario", "status")

    # Filtros laterais disponibilizados no painel administrativo.
    list_filter = ("status", "especialidade", "data")

    # Campos pesquisáveis dentro da área de administração.
    search_fields = ("paciente", "profissional", "telefone", "email")

    # Agrupa registros por data na página administrativa.
    date_hierarchy = "data"

    # Ordenação padrão na listagem.
    ordering = ("data", "horario")

    # Quantidade de registros por página na listagem administrativa.
    list_per_page = 25
