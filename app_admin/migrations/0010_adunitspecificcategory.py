# Generated by Django 3.2.14 on 2023-03-23 04:02

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0009_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdUnitSpecificCategory',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('AdUnitSpecificCategoryId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('VerticalId', models.CharField(blank=True, max_length=50, null=True)),
                ('AdUnitSpecificCategory', models.CharField(max_length=200)),
                ('OrderNo', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
