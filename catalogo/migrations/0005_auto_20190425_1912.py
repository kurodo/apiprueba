# Generated by Django 2.2 on 2019-04-26 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20190425_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]