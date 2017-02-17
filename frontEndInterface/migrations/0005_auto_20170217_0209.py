# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0004_auto_20170217_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='S_news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200, blank=True)),
                ('exc_editor', models.CharField(default=b'\xe6\x9c\xac\xe6\x96\xb0\xe9\x97\xbb\xe6\x89\xa7\xe8\xa1\x8c\xe7\xbc\x96\xe8\xbe\x91', max_length=20)),
                ('duty_editor', models.CharField(default=b'\xe6\x9c\xac\xe6\x96\xb0\xe9\x97\xbb\xe8\xb4\xa3\xe4\xbb\xbb\xe7\xbc\x96\xe8\xbe\x91', max_length=20)),
                ('view_num', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2017, 2, 17, 2, 9, 36, 674805))),
                ('school', models.ForeignKey(to='frontEndInterface.School')),
            ],
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 2, 9, 36, 676787)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 2, 9, 36, 675431)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 2, 9, 36, 677392)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 2, 9, 36, 679335)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 2, 9, 36, 678772)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 2, 9, 36, 672709)),
        ),
    ]
