# Generated by Django 5.1.5 on 2025-01-20 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0006_alter_cardetails_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardetails',
            old_name='image',
            new_name='images',
        ),
    ]
