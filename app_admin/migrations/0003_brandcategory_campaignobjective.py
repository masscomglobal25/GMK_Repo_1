# Generated by Django 3.2.14 on 2023-01-26 00:21

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0002_countryevent_countrynumericcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandCategory',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('BrandCategoryId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('BrandCategory', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignObjective',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('CampaignObjectiveId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('CampaignObjective', models.CharField(max_length=300)),
            ],
        ),
    ]
