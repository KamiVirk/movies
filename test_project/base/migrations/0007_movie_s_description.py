# Generated by Django 4.0 on 2022-02-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_movie_options_alter_movie_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='s_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
