# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-04 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=500)),
                ('prediction', models.IntegerField()),
                ('sentiment', models.IntegerField()),
            ],
        ),
    ]