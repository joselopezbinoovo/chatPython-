# Generated by Django 4.1 on 2022-08-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_chatid_user_chatid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='chatid',
        ),
        migrations.AddField(
            model_name='user',
            name='name2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]