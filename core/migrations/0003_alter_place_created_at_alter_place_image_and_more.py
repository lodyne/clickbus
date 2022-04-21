# Generated by Django 4.0.4 on 2022-04-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_place_created_at_alter_place_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='place',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
