# Generated by Django 2.2 on 2019-05-03 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_auto_20190423_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='monto',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]