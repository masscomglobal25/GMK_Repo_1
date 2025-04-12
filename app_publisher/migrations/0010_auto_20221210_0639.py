# Generated by Django 3.2.14 on 2022-12-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_publisher', '0009_publisherregister_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisherregister',
            name='BannerImage',
            field=models.FileField(blank=True, null=True, upload_to='publisher/banner_image'),
        ),
        migrations.AddField(
            model_name='publisherregister',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publisherregister',
            name='Keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publisherregister',
            name='SeoDescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publisherregister',
            name='Title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
