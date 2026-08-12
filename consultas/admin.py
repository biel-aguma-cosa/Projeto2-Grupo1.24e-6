from django.contrib import admin

from .models import Consulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "profissional", "especialidade", "data", "horario", "status")
    list_filter = ("status", "especialidade", "data")
    search_fields = ("paciente", "profissional", "telefone", "email")
    date_hierarchy = "data"
    ordering = ("data", "horario")
    list_per_page = 25
