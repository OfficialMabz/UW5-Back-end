# Generated by Django 3.0.2 on 2020-08-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0007_auto_20200813_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='teamId',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]