# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('isCompleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('startDate', models.DateTimeField(verbose_name='date published')),
                ('endDate', models.DateTimeField(verbose_name='date published')),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='stage',
            field=models.ManyToManyField(to='process.Stage'),
        ),
        migrations.AddField(
            model_name='process',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.Stage'),
        ),
    ]