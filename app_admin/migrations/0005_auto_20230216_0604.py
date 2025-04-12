# Generated by Django 3.2.14 on 2023-02-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0004_helprequiredfor_meetingrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingrequest',
            name='PublisherId',
        ),
        migrations.AddField(
            model_name='helprequiredfor',
            name='HelpForUser',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetingrequest',
            name='UserId',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='meetingrequest',
            name='UserTypeId',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
