# Generated by Django 4.0.4 on 2022-04-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='updated_at',
            field=models.DateField(),
        ),
    ]
