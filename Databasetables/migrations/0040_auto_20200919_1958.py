# Generated by Django 3.0.2 on 2020-09-19 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0039_auto_20200919_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='ladderId',
            field=models.ForeignKey(blank=True, max_length=220, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Ladder'),
        ),
        migrations.DeleteModel(
            name='PlayerTeam',
        ),
    ]