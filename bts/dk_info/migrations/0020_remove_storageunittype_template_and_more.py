# Generated by Django 4.1.7 on 2023-03-19 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dk_info', '0019_storageunit_storage_unit_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storageunittype',
            name='template',
        ),
        migrations.AddField(
            model_name='storageunittype',
            name='label_template',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
