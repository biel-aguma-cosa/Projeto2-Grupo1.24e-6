"""Configurações do projeto Django.

Este módulo centraliza todas as definições de ambiente, apps instalados,
rotas, banco de dados, templates e arquivos estáticos do sistema.
Ele é o núcleo da aplicação e deve ser consultado sempre que forem feitas
alterações de infraestrutura ou comportamento geral da plataforma.
"""

from pathlib import Path

# Diretório raiz do projeto; usado para localizar templates, arquivos estáticos
# e o banco de dados SQLite.
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta da aplicação. Em produção, esta deve ser substituída por uma
# variável de ambiente segura e não fixa no código.
SECRET_KEY = "django-insecure-agenda-consultas-local"

# Modo de depuração ativo para facilitar o desenvolvimento local.
DEBUG = True

# Hosts permitidos para acesso local. Em produção, devem ser listados de forma
# explícita por segurança.
ALLOWED_HOSTS = []

# Apps instaladas no projeto. O app principal da agenda fica em "consultas".
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "consultas",
]

# Middlewares que processam requisições antes de chegar às views.
# Aqui ficam itens como autenticação, sessão, proteção CSRF e segurança.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Arquivo principal de rotas do projeto.
ROOT_URLCONF = "config.urls"

# Configuração dos templates do Django, incluindo a pasta de templates do
# projeto e os context processors necessários para autenticação e mensagens.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Configuração do WSGI da aplicação para deploy em servidores web.
WSGI_APPLICATION = "config.wsgi.application"

# Banco de dados utilizado pela aplicação. O projeto usa SQLite localmente.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Validações de senha desativadas para simplificar o ambiente local.
AUTH_PASSWORD_VALIDATORS = []

# Idioma e fuso horário do projeto, em português do Brasil.
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Configuração dos arquivos estáticos e da estrutura pública da aplicação.
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Campo automático padrão para modelos com IDs grandes.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
