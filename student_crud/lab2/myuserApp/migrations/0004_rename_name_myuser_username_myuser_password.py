# Generated by Django 4.0.1 on 2022-02-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuserApp', '0003_remove_myuser_issuper'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='myuser',
            name='password',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
