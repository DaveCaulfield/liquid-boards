# Generated by Django 3.2.16 on 2022-11-17 03:20

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_alter_storeaddress_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='logo_image',
            field=cloudinary.models.CloudinaryField(default='logo_placeholder', max_length=255, verbose_name='logo'),
        ),
        migrations.AddField(
            model_name='store',
            name='logo_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]