# Generated by Django 3.2.14 on 2023-02-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vertical_media', '0006_media_webstatsonoff'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='RecommendedMedia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
