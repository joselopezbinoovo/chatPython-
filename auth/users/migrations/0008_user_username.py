# Generated by Django 4.1 on 2022-08-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=30, unique=True, verbose_name='Nome de Usuário'),
            preserve_default=False,
        ),
    ]
