# Generated by Django 5.0.3 on 2024-08-05 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_post_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Tech', max_length=50),
        ),
    ]
