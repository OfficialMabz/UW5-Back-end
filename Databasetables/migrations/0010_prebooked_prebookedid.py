# Generated by Django 3.0.2 on 2020-08-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0009_auto_20200815_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='prebooked',
            name='prebookedId',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]
