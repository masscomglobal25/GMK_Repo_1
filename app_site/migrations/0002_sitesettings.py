# Generated by Django 3.2.14 on 2022-10-20 17:28

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('SiteSettingId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('DefaultCountry', models.CharField(blank=True, max_length=50, null=True)),
                ('DefaultCurrency', models.CharField(blank=True, max_length=50, null=True)),
                ('DefaultTimeZone', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
