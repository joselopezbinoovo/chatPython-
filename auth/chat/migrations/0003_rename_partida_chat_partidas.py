# Generated by Django 4.1 on 2022-08-09 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_partida'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='partida',
            new_name='partidas',
        ),
    ]