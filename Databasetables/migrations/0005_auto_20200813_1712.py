# Generated by Django 3.0.2 on 2020-08-13 16:12

import Databasetables.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0004_auto_20200813_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidates',
            name='Position',
        ),
        migrations.AddField(
            model_name='candidates',
            name='positionId',
            field=models.IntegerField(blank=True, null=True, verbose_name=Databasetables.models.Positions),
        ),
        migrations.AlterField(
            model_name='booking',
            name='locationId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Locations'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='prebookedId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.PreBooked'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='teamAId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Teams'),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='playerId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Players'),
        ),
        migrations.AlterField(
            model_name='challengequeue',
            name='teamId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Teams'),
        ),
        migrations.AlterField(
            model_name='votes',
            name='candidateId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Candidates'),
        ),
        migrations.AlterField(
            model_name='votes',
            name='playerid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Players'),
        ),
        migrations.AlterField(
            model_name='votes',
            name='positionId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Positions'),
        ),
    ]
