# Generated by Django 4.0 on 2022-01-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_movie_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='thumbnails'),
        ),
    ]