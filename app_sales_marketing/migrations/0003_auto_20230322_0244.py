# Generated by Django 3.2.14 on 2023-03-22 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sales_marketing', '0002_salesmarketing_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesmarketing',
            old_name='Name',
            new_name='CompanyName',
        ),
        migrations.AddField(
            model_name='salesmarketing',
            name='MediaName',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
