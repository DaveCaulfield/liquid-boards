# Generated by Django 3.2.16 on 2022-11-19 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_commenter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='excerpt',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
