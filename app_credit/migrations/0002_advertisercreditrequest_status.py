# Generated by Django 3.2.14 on 2022-12-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_credit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisercreditrequest',
            name='Status',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
