# Generated by Django 3.2.9 on 2023-02-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20230215_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='input_output',
            name='hours_work',
            field=models.IntegerField(blank=True, null=True, verbose_name='Horas trabajadas'),
        ),
        migrations.AddField(
            model_name='input_output',
            name='price_work',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Total a pagar'),
        ),
    ]
