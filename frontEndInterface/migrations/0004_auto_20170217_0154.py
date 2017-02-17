# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0003_auto_20170213_0559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'\xe5\xad\xa6\xe6\x9c\xaf\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', max_length=100)),
                ('url', models.CharField(default=b'\xe8\xbf\x99\xe4\xb8\xaa\xe5\xad\xa6\xe6\x9c\xaf\xe6\x89\x80\xe6\x8c\x87\xe5\x90\x91\xe7\x9a\x84url', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'\xe6\x9d\x83\xe7\x9b\x8a\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', max_length=100)),
                ('url', models.CharField(default=b'\xe8\xbf\x99\xe4\xb8\xaa\xe6\x9d\x83\xe7\x9b\x8a\xe5\xad\x97\xe6\xae\xb5\xe6\x89\x80\xe6\x8c\x87\xe5\x90\x91\xe7\x9a\x84url', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SomeElse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_frame', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Thoughts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'\xe6\x80\x9d\xe6\xbd\xae\xe9\x82\xa3\xe4\xb8\x80\xe6\xa0\x8f\xe8\xa6\x81\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6', max_length=100)),
                ('url', models.CharField(default=b'\xe8\xbf\x99\xe4\xb8\xaa\xe6\x80\x9d\xe6\xbd\xae\xe5\xad\x97\xe6\xae\xb5\xe6\x89\x80\xe6\x8c\x87\xe5\x90\x91\xe7\x9a\x84url', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WondPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'\xe5\x9b\xbe\xe7\x89\x87\xe7\x9a\x84\xe6\xa0\x87\xe9\xa2\x98\xef\xbc\x8c\xe4\xb8\x8d\xe8\xa6\x81\xe8\xb6\x85\xe8\xbf\x87100\xe4\xb8\xaa\xe5\xad\x97', max_length=100)),
                ('upload_time', models.DateTimeField(default=datetime.datetime(2017, 2, 17, 1, 54, 12, 302048))),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='WondVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'\xe8\xa7\x86\xe9\xa2\x91\xe7\x9a\x84\xe6\xa0\x87\xe9\xa2\x98', max_length=100)),
                ('compress_image', models.ImageField(upload_to=b'')),
                ('upload_time', models.DateTimeField(default=datetime.datetime(2017, 2, 17, 1, 54, 12, 301504))),
                ('video_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='X_activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
                ('video', models.CharField(max_length=200, blank=True)),
                ('sponsor', models.CharField(max_length=20)),
                ('department', models.ForeignKey(to='frontEndInterface.Department')),
            ],
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 1, 54, 12, 299425)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 1, 54, 12, 298266)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 1, 54, 12, 300164)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 1, 54, 12, 296484)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='video',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
