# Generated by Django 4.1.7 on 2023-03-19 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dk_info', '0016_purchase_order_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseline',
            old_name='count',
            new_name='quantity',
        ),
    ]
