# Generated by Django 3.2.16 on 2022-11-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0014_delete_storelocation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='image_url',
            new_name='store_image_url',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='staff_photo',
        ),
        migrations.RemoveField(
            model_name='store',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='store_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='store',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
