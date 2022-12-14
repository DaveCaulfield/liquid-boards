# Generated by Django 3.2.16 on 2022-11-18 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0010_auto_20221118_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAddress',
            fields=[
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stores.staff')),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('country', models.CharField(max_length=80)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
