# Generated by Django 4.2.1 on 2023-05-30 13:06

import django.contrib.postgres.fields
from django.db import migrations, models
import plant.models
import utilities.validators


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0008_alter_plantimage_image_alter_plantimage_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='other_resources_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(validators=[plant.models.validate_link]), blank=True, null=True, size=5, validators=[plant.models.validate_array_length]),
        ),
        migrations.AlterField(
            model_name='plantimage',
            name='image',
            field=models.ImageField(upload_to=plant.models.get_upload_to, validators=[utilities.validators.ImageValidator(size=1024000)]),
        ),
    ]
