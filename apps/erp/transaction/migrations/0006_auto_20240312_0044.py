# Generated by Django 3.2.5 on 2024-03-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_alter_paymentinstallmentsaletransaction_installment'),
    ]

    operations = [
        migrations.AddField(
            model_name='saletransactionitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Discount'),
        ),
        migrations.AddField(
            model_name='saletransactionitem',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Total Amount'),
        ),
    ]