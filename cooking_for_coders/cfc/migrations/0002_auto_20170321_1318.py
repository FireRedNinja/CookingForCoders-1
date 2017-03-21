# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-21 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cfc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='date',
        ),
        migrations.AddField(
            model_name='recipe',
            name='created',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cfc.DateTime'),
            preserve_default=False,
        ),
    ]