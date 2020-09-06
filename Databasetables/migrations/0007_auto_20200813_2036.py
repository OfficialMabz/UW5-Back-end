# Generated by Django 3.0.2 on 2020-08-13 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0006_auto_20200813_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='bookingId',
        ),
        migrations.RemoveField(
            model_name='cupdraws',
            name='drawID',
        ),
        migrations.RemoveField(
            model_name='cuprounds',
            name='cupRoundId',
        ),
        migrations.RemoveField(
            model_name='fixtures',
            name='fixtureId',
        ),
        migrations.RemoveField(
            model_name='league',
            name='leagueId',
        ),
        migrations.RemoveField(
            model_name='leaguefinals',
            name='gameId',
        ),
        migrations.RemoveField(
            model_name='leaguegames',
            name='gameId',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='locationId',
        ),
        migrations.RemoveField(
            model_name='positions',
            name='positionId',
        ),
        migrations.RemoveField(
            model_name='prebooked',
            name='prebookedId',
        ),
        migrations.AlterField(
            model_name='cupdraws',
            name='teamAId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Teams'),
        ),
        migrations.AlterField(
            model_name='cupdraws',
            name='teamBId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TeamBCupDraws', to='Databasetables.Teams'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='contactforfriendly',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]