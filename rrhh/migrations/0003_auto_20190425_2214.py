# Generated by Django 2.2 on 2019-04-26 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0002_auto_20190425_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puesto',
            name='subordinado',
            field=models.ManyToManyField(blank=True, related_name='_puesto_subordinado_+', to='rrhh.Puesto'),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='superior',
            field=models.ManyToManyField(blank=True, related_name='_puesto_superior_+', to='rrhh.Puesto'),
        ),
    ]
