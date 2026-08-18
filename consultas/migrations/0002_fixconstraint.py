"""Ajusta a regra de unicidade da agenda.

A restrição original permitia conflitos em consultas canceladas. Esta migração
faz com que o mesmo profissional não ocupe o mesmo horário em uma consulta
ativa, preservando cancelamentos sem bloquear a agenda.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='consulta',
            name='consulta_profissional_data_horario_unicos',
        ),
        migrations.AddConstraint(
            model_name='consulta',
            constraint=models.UniqueConstraint(condition=models.Q(('status', 'cancelada'), _negated=True), fields=('profissional', 'data', 'horario'), name='consulta_profissional_data_horario_unicos'),
        ),
    ]
