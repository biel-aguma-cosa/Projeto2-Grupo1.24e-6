import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from consultas.models import Consulta
qs = Consulta.objects.filter(paciente__startswith='Paciente Teste').order_by('criado_em')
print('Encontrados:', qs.count())
for c in qs:
    s = c.especialidade
    print('ANTES:', c.pk, repr(s))
    try:
        repaired = s.encode('latin-1').decode('utf-8')
    except Exception as e:
        print('ENCODE FAIL:', c.pk, e)
        continue
    if repaired != s:
        try:
            c.especialidade = repaired
            c.full_clean()
            c.save()
            print('CORRIGIDO:', c.pk, repr(repaired))
        except Exception as e:
            print('FALHA SALVAR:', c.pk, e)
    else:
        print('SEM ALTERACAO:', c.pk)
print('FIM')
