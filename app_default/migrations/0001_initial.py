# Generated by Django 3.2.14 on 2022-10-08 18:18

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdUnitCategory',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('AdUnitCategoryId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('AdUnitCategory', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CountryType',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('CountryTypeId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('CountryType', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='LightingType',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('LightingTypeId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('LightingType', models.CharField(max_length=310)),
            ],
        ),
        migrations.CreateModel(
            name='MediaAdType',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('MediaAdTypeId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('MediaAdType', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('PackageTypeId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('PackageType', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SiteImageResolution',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('ImageResolutionId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('ImageName', models.CharField(max_length=300)),
                ('Width', models.IntegerField()),
                ('Height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('TimeZoneId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('TimeZone', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('UserTypeId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('UserType', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Vertical',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('VerticalId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('VerticalName', models.CharField(max_length=300)),
                ('VerticalIcon', models.FileField(blank=True, null=True, upload_to='vertical/vertical_icon')),
                ('VerticalEmoji', models.FileField(blank=True, null=True, upload_to='vertical/vertical_emoji')),
                ('VerticalImage', models.FileField(blank=True, null=True, upload_to='vertical/vertical_image')),
                ('RefId', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VerticalStatus',
            fields=[
                ('VerticalStatusId', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('VerticalStatus', models.CharField(max_length=300)),
            ],
        ),
    ]
