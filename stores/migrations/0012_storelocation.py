# Generated by Django 3.2.16 on 2022-11-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0011_staffaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
