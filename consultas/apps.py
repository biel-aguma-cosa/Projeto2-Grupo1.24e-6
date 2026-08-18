"""Configuração do aplicativo de agenda de consultas."""

from django.apps import AppConfig


class ConsultasConfig(AppConfig):
    """Define as configurações do app principal do sistema."""

    # Campo padrão para chaves primárias dos modelos do app.
    default_auto_field = "django.db.models.BigAutoField"
    # Nome do app em Python, usado pelo Django para identificar o módulo.
    name = "consultas"
    # Nome amigável exibido em telas administrativas e logs do Django.
    verbose_name = "Agenda de consultas"
