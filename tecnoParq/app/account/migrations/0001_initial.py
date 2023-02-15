# Generated by Django 3.2.9 on 2023-02-15 09:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('identify', models.BigIntegerField(verbose_name='Cedula')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('username', models.CharField(max_length=100, verbose_name='Nombre de usuario')),
                ('password', models.CharField(max_length=100, verbose_name='Contraseña')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Input_Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date_in', models.DateField(auto_now_add=True, verbose_name='Fecha de entrada')),
                ('time_in', models.TimeField(blank=True, null=True, verbose_name='Hora de entrada')),
                ('date_out', models.DateField(blank=True, null=True, verbose_name='Fecha de salida')),
                ('time_out', models.TimeField(blank=True, null=True, verbose_name='Hora de salida')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]