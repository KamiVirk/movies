# Generated by Django 4.0 on 2022-02-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_movie_options_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(default='default.png', upload_to='thumbnails'),
        ),
    ]
