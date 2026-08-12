from django.urls import path

from . import views

app_name = "consultas"

urlpatterns = [
    path("", views.lista_consultas, name="lista"),
    path("nova/", views.criar_consulta, name="criar"),
    path("<int:pk>/editar/", views.editar_consulta, name="editar"),
    path("<int:pk>/excluir/", views.excluir_consulta, name="excluir"),
]
