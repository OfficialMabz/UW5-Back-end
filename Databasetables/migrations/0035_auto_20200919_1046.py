# Generated by Django 3.0.2 on 2020-09-19 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Databasetables', '0034_auto_20200919_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='ladderId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Databasetables.Ladder'),
        ),
    ]