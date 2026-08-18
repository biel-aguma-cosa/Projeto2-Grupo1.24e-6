# Agenda de Consultas

Sistema web para gestão de agenda de uma clínica, desenvolvido em Django com Bootstrap 5. O projeto centraliza o cadastro, consulta, edição e exclusão de atendimentos, além de fornecer uma visão geral por status e filtros de busca.

## Visão geral

A aplicação foi pensada para facilitar a rotina administrativa da clínica:

- consultar rapidamente todas as consultas agendadas;
- buscar por paciente, profissional ou especialidade;
- filtrar por status da consulta;
- cadastrar novas consultas;
- editar dados existentes;
- remover registros com confirmação;
- evitar conflitos de agenda para o mesmo profissional no mesmo horário.

## Tecnologias utilizadas

- Python
- Django 6.1
- SQLite
- Bootstrap 5
- HTML, CSS e JavaScript

## Estrutura do projeto

```text
Projeto2-Grupo1.24e-6/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── consultas/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── static/
│   └── css/
│       └── app.css
├── templates/
│   ├── base.html
│   └── consultas/
│       ├── form.html
│       ├── lista.html
│       └── confirmacao.html
├── db.sqlite3
├── manage.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Fluxo principal da aplicação

### 1. Configuração geral
O arquivo [config/settings.py](config/settings.py) concentra as configurações do projeto, como:

- apps instalados;
- banco de dados SQLite;
- templates;
- arquivos estáticos;
- timezone e idioma;
- configuração principal do Django.

### 2. Rotas da aplicação
O arquivo [config/urls.py](config/urls.py) define as rotas globais do sistema.

- `/admin/` → área administrativa do Django;
- `/` → página principal da agenda do app `consultas`.

As rotas específicas do app ficam em [consultas/urls.py](consultas/urls.py):

- `/` → listagem de consultas;
- `/nova/` → cadastro de consulta;
- `/<id>/editar/` → edição;
- `/<id>/excluir/` → exclusão.

### 3. Modelo principal
A entidade central do projeto está em [consultas/models.py](consultas/models.py).

A classe `Consulta` representa uma consulta médica com os seguintes campos:

- `paciente`: nome do paciente;
- `telefone`: contato telefônico;
- `email`: e-mail do paciente;
- `profissional`: nome do profissional responsável;
- `especialidade`: área do atendimento;
- `data`: data da consulta;
- `horario`: hora do atendimento;
- `status`: agendada, confirmada, realizada ou cancelada;
- `observacoes`: detalhes extras;
- `criado_em`: data de criação;
- `atualizado_em`: data da última alteração.

### 4. Regras de negócio
O modelo possui uma validação importante:

- não pode haver duas consultas ativas do mesmo profissional na mesma data e horário;
- consultas canceladas não entram nessa regra;
- isso evita conflitos de agenda.

Essa lógica é implementada com `UniqueConstraint` e validação no método `clean()`.

### 5. Formulário de entrada
O formulário está em [consultas/forms.py](consultas/forms.py).

Ele controla:

- campos exibidos ao usuário;
- widgets HTML para data, horário e observações;
- classes CSS do Bootstrap;
- entrada no formato brasileiro (`dd/mm/yyyy` e `HH:MM`).

### 6. Views e fluxo web
As views estão em [consultas/views.py](consultas/views.py).

#### `lista_consultas`
- busca todas as consultas;
- aplica filtro por texto;
- aplica filtro por status;
- ordena por coluna selecionada;
- envia dados para o template da agenda.

#### `criar_consulta`
- recebe os dados do formulário;
- valida o formulário;
- salva a nova consulta;
- redireciona para a lista.

#### `editar_consulta`
- carrega a consulta pelo ID;
- reaproveita o `ConsultaForm` com a instância atual;
- salva as alterações no banco.

#### `excluir_consulta`
- busca a consulta pelo ID;
- exige confirmação via formulário ou modal;
- remove o registro.

### 7. Templates e UI
A interface é organizada em templates Django:

- [templates/base.html](templates/base.html): estrutura base da página, navbar e carregamento de CSS/JS;
- [templates/consultas/lista.html](templates/consultas/lista.html): página principal da agenda com filtros, cards e tabela;
- [templates/consultas/form.html](templates/consultas/form.html): formulário de criação/edição;
- [templates/consultas/confirmacao.html](templates/consultas/confirmacao.html): página de confirmação de exclusão.

A estilização principal está em [static/css/app.css](static/css/app.css).

## Status disponíveis

A aplicação usa os seguintes status:

- `agendada`
- `confirmada`
- `realizada`
- `cancelada`

Esses valores são definidos em `Consulta.Status` em [consultas/models.py](consultas/models.py).

## Administração do Django

A área administrativa do Django está ativa em `/admin/` e foi configurada em [consultas/admin.py](consultas/admin.py).

Esse arquivo define como a entidade `Consulta` aparece no painel administrativo, incluindo:

- colunas exibidas;
- filtros;
- busca;
- página por página;
- ordenação padrão.

## Como rodar o projeto localmente

No terminal, dentro da pasta do projeto:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Depois, acesse:

```text
http://127.0.0.1:8000/
```

Para criar um usuário administrador:

```bash
python manage.py createsuperuser
```

## Dicas para manutenção e onboarding

- Sempre aloque alterações de regra de negócio no modelo e, se necessário, nas views.
- Para alterações visuais, priorize [static/css/app.css](static/css/app.css) e os templates.
- Use os dados de `status` e `especialidade` como fonte de verdade da aplicação.
- Antes de alterar a modelagem, verifique se há impactos nas migrações e no banco existente.
- A validação de conflitos deve permanecer ativa para evitar duplicidade de horários.

## Observações finais

Este projeto é uma aplicação simples, porém bem organizada para uso administrativo e controle clínico básico. O código está estruturado para ser facilmente lido por outros funcionários e para evoluir sem quebrar a lógica de funcionamento da agenda.

