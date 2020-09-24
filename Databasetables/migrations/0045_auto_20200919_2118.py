# Generated by Django 3.0.2 on 2020-09-19 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0044_auto_20200919_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='competitionId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='ladderId',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Ladder'),
        ),
    ]
