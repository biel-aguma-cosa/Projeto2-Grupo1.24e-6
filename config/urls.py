"""URLs globais do projeto.

Aqui são registradas as rotas principais do sistema. A área administrativa do
Django é exposta em /admin/ e o restante da aplicação é organizada no app
"consultas" via include().
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Área administrativa padrão do Django.
    path("admin/", admin.site.urls),
    # Inclui as rotas do app de agenda/consultas na raiz do site.
    path("", include("consultas.urls")),
]
