# Generated by Django 3.2.14 on 2023-03-19 21:23

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_default', '0008_adunitcategory_orderno'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotAavatar',
            fields=[
                ('SortId', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('BotAavatarId', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('BotAavatar', models.FileField(blank=True, null=True, upload_to='bot/default')),
            ],
        ),
    ]
