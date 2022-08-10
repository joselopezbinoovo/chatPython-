# Generated by Django 4.1 on 2022-08-09 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        ('users', '0004_remove_user_chatid_user_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name2',
        ),
        migrations.AddField(
            model_name='user',
            name='chatid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chat.chat'),
            preserve_default=False,
        ),
    ]