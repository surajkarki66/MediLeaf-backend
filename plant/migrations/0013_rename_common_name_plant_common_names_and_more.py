# Generated by Django 4.2.1 on 2023-06-03 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0012_merge_20230603_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='common_name',
            new_name='common_names',
        ),
        migrations.RenameField(
            model_name='plant',
            old_name='common_name_ne',
            new_name='common_names_ne',
        ),
    ]
