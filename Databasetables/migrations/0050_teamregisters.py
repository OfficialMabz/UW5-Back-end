# Generated by Django 3.0.2 on 2020-09-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0049_auto_20200924_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamRegisters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(default='0', max_length=50)),
                ('teampassword', models.CharField(default='0', max_length=50)),
            ],
        ),
    ]