# Generated by Django 3.2.14 on 2023-03-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sales_marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesmarketing',
            name='Country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
