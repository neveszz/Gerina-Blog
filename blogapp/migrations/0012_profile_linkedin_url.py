# Generated by Django 5.0.3 on 2024-08-07 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_profile_instagram_url_profile_profile_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
