# Generated by Django 3.2.14 on 2022-11-11 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_publisher', '0007_publisherregister_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishercontact',
            name='PhoneCode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
