# Generated by Django 2.2 on 2019-04-30 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0014_auto_20190429_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodcutovariacion',
            name='codigo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='codigo',
            field=models.IntegerField(default=0),
        ),
    ]