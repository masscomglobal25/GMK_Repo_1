# Generated by Django 3.2.14 on 2023-04-17 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertiser', '0007_alter_profile_creditsexpirydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='IsUpgrade',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
