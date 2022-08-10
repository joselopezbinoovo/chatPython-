# Generated by Django 4.1 on 2022-08-09 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chatId',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='chat.chat'),
            preserve_default=False,
        ),
    ]