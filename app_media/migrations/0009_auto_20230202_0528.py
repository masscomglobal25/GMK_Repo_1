# Generated by Django 3.2.14 on 2023-02-02 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_media', '0008_auto_20230129_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='MediaLink',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='SourceFrom',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plandetail',
            name='MediaLink',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plandetail',
            name='SourceFrom',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
