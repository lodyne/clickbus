# Generated by Django 4.0.4 on 2022-04-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_place_created_at_alter_place_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
