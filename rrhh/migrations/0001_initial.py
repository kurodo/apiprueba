# Generated by Django 2.2 on 2019-04-26 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(blank=True, max_length=8)),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('correo', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('salario', models.IntegerField()),
                ('modalidad', models.CharField(choices=[('hor', 'Hora'), ('sem', 'Semanal'), ('qui', 'Quincenal'), ('men', 'Mensual'), ('pro', 'Produccion')], max_length=5)),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.Trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('subordinado', models.ManyToManyField(blank=True, null=True, related_name='_puesto_subordinado_+', to='rrhh.Puesto')),
                ('superior', models.ManyToManyField(blank=True, null=True, related_name='_puesto_superior_+', to='rrhh.Puesto')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.Trabajador')),
            ],
        ),
    ]
