# Generated by Django 4.2.1 on 2023-05-31 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0010_alter_plantspecies_genus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantspecies',
            name='genus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species', to='plant.plantgenus'),
        ),
    ]
