# Generated by Django 3.2.14 on 2022-10-10 20:14

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_default', '0002_serviceorderunit_serviceunittype'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffPermission',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('StaffPermissionId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('StaffPermission', models.CharField(max_length=300)),
            ],
        ),
    ]
