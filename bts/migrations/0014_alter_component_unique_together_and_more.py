# Generated by Django 4.1.7 on 2023-04-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bts', '0013_alter_storageunitcompartment_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='component',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='component',
            constraint=models.UniqueConstraint(fields=('part_number', 'merchant'), name='UQ_Component_part_number_merchant'),
        ),
    ]
