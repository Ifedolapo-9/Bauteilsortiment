# Generated by Django 4.1.7 on 2023-03-23 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bts', '0005_rename_storage_unit_compartment_subcomponent_storage_unit_compartments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcomponent',
            name='storage_unit_compartments',
        ),
    ]