# Generated by Django 3.2.4 on 2021-06-25 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='pwd',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
    ]
