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
            name='AdFormat',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('AdFormatId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('AdFormat', models.CharField(max_length=300)),
                ('VerticalId', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AdunitPosition',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('AdunitPositionId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('AdunitPosition', models.CharField(max_length=300)),
                ('VerticalId', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AdunitSize',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('AdunitSizeId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('AdunitSize', models.CharField(max_length=300)),
                ('VerticalId', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('AgeGroupId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('AgeGroup', models.CharField(max_length=300)),
                ('AgeGroupIcon', models.FileField(blank=True, null=True, upload_to='AgeGroup')),
            ],
        ),
        migrations.CreateModel(
            name='CityRegion',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('CityId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('CountryId', models.CharField(max_length=50)),
                ('CityRegionName', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CountryEvent',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('CountryEventId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('CountryType', models.CharField(blank=True, max_length=50, null=True)),
                ('CountryEventName', models.CharField(blank=True, max_length=300, null=True)),
                ('CountryCode', models.CharField(blank=True, max_length=10, null=True)),
                ('TelephoneCode', models.CharField(blank=True, max_length=10, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('GeneralInfo', models.TextField(blank=True, null=True)),
                ('Logo', models.FileField(blank=True, null=True, upload_to='CountryEvent')),
                ('InfoImage', models.FileField(blank=True, null=True, upload_to='CountryEvent')),
                ('BannerImage', models.FileField(blank=True, null=True, upload_to='CountryEvent')),
                ('StartDate', models.CharField(blank=True, max_length=400, null=True)),
                ('EndDate', models.CharField(blank=True, max_length=400, null=True)),
                ('MatchingCategoriesToAd', models.TextField(blank=True, null=True)),
                ('AvailableVertical', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstimatedReach',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('EstimatedReachId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('EstimatedReach', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='GenderGroup',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('GenderGroupId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('GenderGroup', models.CharField(max_length=300)),
                ('GenderGroupIcon', models.FileField(blank=True, null=True, upload_to='GenderGroup')),
            ],
        ),
        migrations.CreateModel(
            name='IncomeGroup',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('IncomeGroupId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('IncomeGroup', models.CharField(max_length=300)),
                ('IncomeGroupIcon', models.FileField(blank=True, null=True, upload_to='IncomeGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('LanguageId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('Language', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('LocationTypeId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('LocationType', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MatchingCategory',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('MatchingCategoryId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('MatchingCategory', models.CharField(max_length=300)),
                ('CategoryIcon', models.FileField(blank=True, null=True, upload_to='MatachingCategory')),
            ],
        ),
        migrations.CreateModel(
            name='MediaCategory',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('MediaCategoryId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('MediaCategory', models.CharField(max_length=300)),
                ('VerticalId', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='NationalityCommunity',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('NationalityCommunityId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('NationalityCommunity', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='NearByAdvantage',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('NearByAdvantageId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('NearByAdvantage', models.CharField(max_length=300)),
                ('NearByAdvantageIcon', models.FileField(blank=True, null=True, upload_to='NearByAdvantage')),
            ],
        ),
        migrations.CreateModel(
            name='StaffRegister',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('StaffId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('EmailId', models.CharField(max_length=300)),
                ('Name', models.CharField(max_length=300)),
                ('UserGroup', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VerticalType',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('VerticalTypeId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('VerticalId', models.CharField(max_length=50)),
                ('VerticalType', models.CharField(max_length=300)),
            ],
        ),
    ]
