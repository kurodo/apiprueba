# Generated by Django 2.2 on 2019-04-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_producto_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]