# Generated by Django 4.0.3 on 2023-07-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0003_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Verified'),
        ),
    ]
