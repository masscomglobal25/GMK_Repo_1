# Generated by Django 3.2.14 on 2023-04-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_publisher', '0017_publisherregister_bannerimageformobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisherregister',
            name='EnableMediaEntry',
            field=models.BooleanField(default=False),
        ),
    ]
