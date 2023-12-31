# Generated by Django 4.2.1 on 2023-06-14 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_colaborador_data_rescisao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastrado', models.DateField()),
                ('id_processo', models.IntegerField(unique=True)),
                ('tipo_atuacao', models.CharField(choices=[('PERÍCIA LIQUIDAÇÃO', 'PERÍCIA LIQUIDAÇÃO'), ('PERÍCIA INSTRUÇÃO', 'PERÍCIA INSTRUÇÃO'), ('PERÍCIA CONHECIMENTO', 'PERÍCIA CONHECIMENTO'), ('PERÍCIA CÍVEL', 'PERÍCIA CÍVEL'), ('ASSISTÊNCIA TÉCNICA PARTE 1', 'ASSISTÊNCIA TÉCNICA PARTE 1'), ('ASSISTÊNCIA TÉCNICA PARTE 2', 'ASSISTÊNCIA TÉCNICA PARTE 2'), ('ASSISTÊNCIA CONTRATO TRABALHO', 'ASSISTÊNCIA CONTRATO TRABALHO'), ('TERCEIRIZAÇÃO', 'TERCEIRIZAÇÃO'), ('ADMINISTRAÇÃO JUDICIAL', 'ADMINISTRAÇÃO JUDICIAL'), ('MUTIRÃO TRT6', 'MUTIRÃO TRT6'), ('EXECUÇÃO DE TÍTULO JUDICIAL', 'EXECUÇÃO DE TÍTULO JUDICIAL')], max_length=50)),
                ('numero_processo', models.CharField(max_length=25, unique=True)),
                ('tipo_acao', models.CharField(choices=[('RECLAMAÇÃO TRABALHISTA', 'RECLAMAÇÃO TRABALHISTA'), ('EXECUÇÃO PROVISÓRIA', 'EXECUÇÃO PROVISÓRIA'), ('CONSIGNAÇÃO EM PAGAMENTO', 'CONSIGNAÇÃO EM PAGAMENTO'), ('AÇÃO DE CUMPRIMENTO', 'AÇÃO DE CUMPRIMENTO'), ('CUMPRIMENTO DE SENTENÇA', 'CUMPRIMENTO DE SENTENÇA'), ('PROCEDIMENTO COMUM CÍVEL', 'PROCEDIMENTO COMUM CÍVEL'), ('AÇÃO MONITÓRIA', 'AÇÃO MONITÓRIA'), ('AÇÃO CIVIL COLETIVA', 'AÇÃO CIVIL COLETIVA'), ('AÇÃO CIVIL PÚBLICA', 'AÇÃO CIVIL PÚBLICA')], max_length=50)),
                ('tipo_processo', models.CharField(choices=[('PJe', 'PJe'), ('PJe-n', 'PJe-n'), ('CSV', 'CSV'), ('CSV-n', 'CSV-n'), ('CSV-AF', 'CSV-AF'), ('Físico', 'Físico')], max_length=50)),
                ('parte_1', models.TextField()),
                ('parte_2', models.TextField()),
                ('processos_associados', models.IntegerField()),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('responsavel_cadastrado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.colaborador')),
            ],
            options={
                'verbose_name_plural': 'Processo',
            },
        ),
    ]
