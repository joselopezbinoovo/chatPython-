# Generated by Django 4.1 on 2022-08-09 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0002_partida_nombre'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='partida',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='partidas.partida'),
            preserve_default=False,
        ),
    ]