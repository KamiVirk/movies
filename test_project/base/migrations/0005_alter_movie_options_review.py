# Generated by Django 4.0 on 2022-02-10 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0004_movie_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-update', '-created']},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, '1 - Trash'), (2, '2 - Terrible'), (3, '3 - Horrible'), (4, '4 - Bad'), (5, '5 - Ok'), (6, '6 - Watchable'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Master Piece')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.movie')),
                ('r_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
