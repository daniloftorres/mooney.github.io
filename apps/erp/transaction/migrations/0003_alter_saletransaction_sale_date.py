# Generated by Django 3.2.5 on 2024-03-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20240311_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saletransaction',
            name='sale_date',
            field=models.DateTimeField(null=True, verbose_name='Sale Date'),
        ),
    ]