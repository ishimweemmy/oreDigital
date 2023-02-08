# Generated by Django 3.2.12 on 2023-02-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0003_alter_incident_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='id',
        ),
        migrations.AlterField(
            model_name='incident',
            name='incidentId',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]