# Generated by Django 3.0.2 on 2020-09-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0025_auto_20200904_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ladder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LadderName', models.CharField(max_length=50)),
            ],
        ),
    ]
