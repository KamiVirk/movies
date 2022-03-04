# Generated by Django 4.0 on 2022-01-18 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('long_description', models.TextField(blank=True, null=True)),
                ('video_url', models.URLField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('movie_genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category')),
            ],
        ),
    ]
