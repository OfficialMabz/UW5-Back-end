# Generated by Django 3.0.2 on 2020-08-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0008_teams_teamid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='teamId',
        ),
        migrations.AlterField(
            model_name='prebooked',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]