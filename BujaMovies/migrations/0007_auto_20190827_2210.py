# Generated by Django 2.2.3 on 2019-08-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BujaMovies', '0006_auto_20190827_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avis',
            name='likes',
            field=models.BooleanField(default=False),
        ),
    ]
