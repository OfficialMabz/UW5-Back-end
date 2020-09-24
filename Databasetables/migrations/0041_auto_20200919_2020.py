# Generated by Django 3.0.2 on 2020-09-19 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0040_auto_20200919_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='ladderId',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Ladder'),
        ),
        migrations.CreateModel(
            name='PlayerTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('goalsScored', models.IntegerField(null=True)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Teams')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Databasetables.PlayerProfile')),
            ],
        ),
    ]
