# Generated by Django 4.0.4 on 2022-05-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Квентин тарантино', max_length=100),
        ),
    ]
