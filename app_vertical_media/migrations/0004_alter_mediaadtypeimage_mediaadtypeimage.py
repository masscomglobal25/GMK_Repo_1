# Generated by Django 3.2.14 on 2023-01-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vertical_media', '0003_mediaadtype_ratedisplay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaadtypeimage',
            name='MediaAdTypeImage',
            field=models.FileField(blank=True, null=True, upload_to='vertical/media/image'),
        ),
    ]
