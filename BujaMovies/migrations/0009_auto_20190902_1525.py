# Generated by Django 2.2.3 on 2019-09-02 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BujaMovies', '0008_auto_20190827_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avis',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Slug_F', to='BujaMovies.Films')),
                ('titre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Titre_F', to='BujaMovies.Films')),
            ],
        ),
    ]
