# Generated by Django 3.0.2 on 2020-08-25 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0021_remove_playerprofile_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='playerprofile',
            name='phone',
        ),
    ]