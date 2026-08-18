"""Migração inicial da aplicação de consultas.

Cria a tabela principal do sistema e registra os campos básicos da agenda,
como paciente, profissional, data, horário e status.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=120, verbose_name='paciente')),
                ('telefone', models.CharField(blank=True, max_length=20, verbose_name='telefone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('profissional', models.CharField(max_length=120, verbose_name='profissional')),
                ('especialidade', models.CharField(max_length=100, verbose_name='especialidade')),
                ('data', models.DateField(verbose_name='data')),
                ('horario', models.TimeField(verbose_name='horario')),
                ('status', models.CharField(choices=[('agendada', 'Agendada'), ('confirmada', 'Confirmada'), ('realizada', 'Realizada'), ('cancelada', 'Cancelada')], default='agendada', max_length=12, verbose_name='status')),
                ('observacoes', models.TextField(blank=True, verbose_name='observacoes')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
            ],
            options={
                'verbose_name': 'consulta',
                'verbose_name_plural': 'consultas',
                'ordering': ['data', 'horario'],
                'constraints': [models.UniqueConstraint(fields=('profissional', 'data', 'horario'), name='consulta_profissional_data_horario_unicos')],
            },
        ),
    ]
