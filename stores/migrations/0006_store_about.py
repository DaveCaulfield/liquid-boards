# Generated by Django 3.2.16 on 2022-11-17 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_auto_20221117_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='about',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]