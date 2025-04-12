# Generated by Django 3.2.14 on 2022-10-28 00:24

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_publisher', '0005_publisherregister_regby'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRequest',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('MeetingRequestId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('AdvertiserId', models.CharField(max_length=50)),
                ('PublisherId', models.CharField(max_length=50)),
                ('PublisherContactId', models.CharField(max_length=50)),
                ('PreferredContact', models.CharField(max_length=50)),
                ('HelpRequiredFor', models.TextField()),
                ('FromDate', models.CharField(max_length=50)),
                ('FromTime', models.CharField(max_length=50)),
                ('ToDate', models.CharField(max_length=50)),
                ('ToTime', models.CharField(max_length=50)),
                ('TimeZone', models.CharField(max_length=100)),
                ('Message', models.TextField()),
                ('CreatedDate', models.CharField(max_length=200)),
            ],
        ),
    ]
