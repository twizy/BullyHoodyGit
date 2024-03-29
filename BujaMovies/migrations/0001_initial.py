# Generated by Django 2.2.3 on 2019-08-26 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30, verbose_name='Titre')),
                ('acteur', models.CharField(max_length=25, verbose_name='Acteur principale')),
                ('description', models.TextField(verbose_name='Description')),
                ('language', models.TextField(verbose_name='Language')),
                ('resolution', models.IntegerField(verbose_name='Resolution')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField(verbose_name='Commenter')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('titre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BujaMovies.Films', verbose_name='Choisir Titre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liké', models.TextField(verbose_name="J'aime")),
                ('disliké', models.TextField(verbose_name="J'aime pas")),
                ('titre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BujaMovies.Films', verbose_name='Choisir Titre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
