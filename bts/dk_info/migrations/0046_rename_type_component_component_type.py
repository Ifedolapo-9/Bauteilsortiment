# Generated by Django 4.1.7 on 2023-03-21 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dk_info', '0045_alter_component_part_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='component',
            old_name='type',
            new_name='component_type',
        ),
    ]
