# Generated by Django 4.0.1 on 2022-02-01 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]