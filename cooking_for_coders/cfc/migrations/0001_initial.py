# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-21 15:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Recipe', max_length=128)),
                ('recipeID', models.IntegerField(unique=True)),
                ('ingredients', models.TextField(default='Put your ingredients here!')),
                ('instructions', models.TextField(default='Type your instructions here!')),
                ('description', models.CharField(default='Put a short description here!', max_length=64)),
                ('picture', models.ImageField(blank=True, upload_to='media/recipe/')),
                ('rating', models.IntegerField(blank=True, default=0)),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 3, 21, 15, 28, 5, 182665, tzinfo=utc))),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfc.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SavedRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfc.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountID', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=128)),
                ('profile_picture', models.ImageField(default='static/images/default.jpg', upload_to='static/images/profile_pictures')),
                ('my_recipes', models.CharField(blank=True, default=0, max_length=128)),
                ('saved_recipes', models.CharField(blank=True, default=0, max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='savedrecipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfc.UserProfile'),
        ),
    ]
