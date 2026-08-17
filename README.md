# Agenda de Consultas

Sistema web para cadastro e acompanhamento de consultas de uma clínica, construído com Django e Bootstrap 5.

## Funcionalidades

- Listagem com busca por paciente, profissional ou especialidade.
- Filtro por status e indicadores resumidos da agenda.
- Cadastro, edição e exclusão de consultas.
- Validação para impedir dois atendimentos do mesmo profissional no mesmo horário.
- Django Admin disponível em `/admin/`.

## Executar localmente

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/`. Para criar um usuário administrador, execute `python manage.py createsuperuser`.


paciente:
- nome
- sobrenome
- opcional:
    - telefone
    - email
    - senha 
profissional:
- nome
- sobrenome
- qualificações
consulta:
- paciente
- profissional
- data
- hora
- assunto
- detalhes
- estado

