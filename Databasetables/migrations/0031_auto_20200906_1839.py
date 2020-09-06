# Generated by Django 3.0.2 on 2020-09-06 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0030_auto_20200905_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='goals_scored',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='phone',
            field=models.IntegerField(blank=True, default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='ladder',
            name='LadderName',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='teams',
            name='ladderId',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Ladder'),
        ),
    ]