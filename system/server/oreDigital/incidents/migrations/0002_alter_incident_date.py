# Generated by Django 3.2.12 on 2023-02-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
