# Generated by Django 4.0.1 on 2022-02-01 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuserApp', '0005_alter_myuser_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myuser',
            new_name='Superuser',
        ),
    ]