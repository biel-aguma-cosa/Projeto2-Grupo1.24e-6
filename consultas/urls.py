"""Rotas do app de consultas.

Estas URLs controlam a navegação principal da agenda:
- listagem das consultas;
- criação de novas consultas;
- edição;
- exclusão.
"""

from django.urls import path

from . import views

app_name = "consultas"

urlpatterns = [
    # Página inicial da agenda com listagem e filtros.
    path("", views.lista_consultas, name="lista"),
    # Rota para cadastrar uma nova consulta.
    path("nova/", views.criar_consulta, name="criar"),
    # Rota para editar uma consulta existente.
    path("<int:pk>/editar/", views.editar_consulta, name="editar"),
    # Rota para confirmar e excluir uma consulta.
    path("<int:pk>/excluir/", views.excluir_consulta, name="excluir"),
]
