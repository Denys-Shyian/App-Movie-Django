# Generated by Django 4.0.4 on 2022-05-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_alter_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director_email',
            field=models.EmailField(default='sugar_daddy@gmail.com', max_length=254),
        ),
    ]