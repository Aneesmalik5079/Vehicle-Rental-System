# Generated by Django 5.1.5 on 2025-01-20 11:48

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0009_rename_images_cardetails_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bikedetails',
            fields=[
                ('rent_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bikename', models.TextField()),
                ('brand', models.TextField()),
                ('year', models.IntegerField(null=True)),
                ('price', models.IntegerField()),
                ('fueltype', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='bike_images')),
                ('dealer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
