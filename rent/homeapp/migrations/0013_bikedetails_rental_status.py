# Generated by Django 5.1.5 on 2025-01-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0012_rentedbikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikedetails',
            name='rental_status',
            field=models.CharField(choices=[('Not Rented', 'Not Rented'), ('Rented', 'Rented')], default='Not Rented', max_length=20),
        ),
    ]
