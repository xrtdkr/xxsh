# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('introduction', models.TextField()),
                ('image', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 12, 14, 46, 6, 14653))),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_url', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'\xe9\x83\xa8\xe9\x97\xa8\xe7\x9a\x84\xe5\x90\x8d\xe5\xad\x97', max_length=20)),
                ('introduction', models.TextField(default=b'\xe8\xbf\x99\xe6\x98\xaf\xe7\xae\x80\xe4\xbb\x8b')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 12, 14, 46, 6, 13390))),
                ('view_num', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('exc_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20)),
                ('duty_editor', models.CharField(default=b'\xe6\x9c\xac\xe5\x85\xac\xe5\x91\x8a\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Safeguard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'\xe7\xbb\xb4\xe6\x9d\x83\xe8\x80\x85\xe5\x90\x8d\xe5\xad\x97', max_length=20)),
                ('title', models.CharField(default=b'\xe7\xbb\xb4\xe6\x9d\x83\xe4\xb8\xbb\xe9\xa2\x98', max_length=200)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 12, 14, 46, 6, 15995))),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('introduction', models.TextField()),
                ('chef', models.CharField(max_length=20)),
                ('chef_introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'\xe7\xbb\x84\xe5\x91\x98\xe5\x90\x8d\xe5\xad\x97', max_length=20)),
                ('grade', models.CharField(default=b'', max_length=20)),
                ('rank', models.CharField(default=b'', max_length=20)),
                ('introduction', models.TextField()),
                ('image', models.CharField(max_length=200)),
                ('chef_flag', models.BooleanField(default=False)),
                ('department', models.ForeignKey(to='frontEndInterface.Department')),
            ],
        ),
        migrations.CreateModel(
            name='x_news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
                ('exc_editor', models.CharField(default=b'\xe6\x9c\xac\xe6\x96\xb0\xe9\x97\xbb\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20)),
                ('duty_editor', models.CharField(default=b'\xe6\x9c\xac\xe6\x96\xb0\xe9\x97\xbb\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20)),
                ('view_num', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 12, 14, 46, 6, 12248))),
                ('department', models.ForeignKey(to='frontEndInterface.Department')),
            ],
        ),
    ]
