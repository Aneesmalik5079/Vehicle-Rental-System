# Generated by Django 5.1.5 on 2025-01-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0013_bikedetails_rental_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetails',
            name='rental_status',
            field=models.CharField(choices=[('Not Rented', 'Not Rented'), ('Rented', 'Rented')], default='Not Rented', max_length=20),
        ),
    ]
