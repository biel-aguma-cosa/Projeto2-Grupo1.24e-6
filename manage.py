#!/usr/bin/env python
"""Ponto de entrada principal do projeto Django.

Este arquivo inicializa o ambiente de execução do Django e delega o controle
para o gerenciador de comandos do framework. Ele é responsável por carregar as
configurações do projeto e executar tarefas como migrations, runserver e
criação de superusuário.
"""

import os
import sys


def main():
    """Executa o comando principal do Django para o projeto."""
    # Define o módulo de configurações do projeto para o ambiente do Django.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        # Importa o executador de comandos do Django apenas quando necessário.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Mensagem clara caso o Django ainda não esteja instalado no ambiente.
        raise ImportError("Django nao esta instalado.") from exc

    # Processa os argumentos da linha de comando, como runserver, migrate e shell.
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
