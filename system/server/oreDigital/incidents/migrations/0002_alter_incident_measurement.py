# Generated by Django 3.2.12 on 2023-02-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='measurement',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]