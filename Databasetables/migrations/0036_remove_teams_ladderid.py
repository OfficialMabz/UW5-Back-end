# Generated by Django 3.0.2 on 2020-09-19 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0035_auto_20200919_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='ladderId',
        ),
    ]
