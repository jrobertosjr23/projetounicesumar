# Generated by Django 4.2.1 on 2023-06-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_colaborador_data_rescisao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='data_rescisao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
