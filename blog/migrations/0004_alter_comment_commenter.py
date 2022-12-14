# Generated by Django 3.2.16 on 2022-11-16 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userprofile_default_full_name'),
        ('blog', '0003_comment_commenter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='profiles.userprofile'),
        ),
    ]
