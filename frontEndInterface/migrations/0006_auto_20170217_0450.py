# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0005_auto_20170217_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='image_url',
        ),
        migrations.AddField(
            model_name='carousel',
            name='image',
            field=models.ImageField(default=None, upload_to=b'carousel'),
        ),
        migrations.AddField(
            model_name='information',
            name='image',
            field=models.ImageField(default=None, upload_to=b'information'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 4, 50, 47, 854044)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image',
            field=models.ImageField(upload_to=b'apply'),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 4, 50, 47, 852486)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 4, 50, 47, 851771)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='image',
            field=models.ImageField(upload_to=b'snews'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 4, 50, 47, 854715)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(upload_to=b'staff'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='image',
            field=models.ImageField(upload_to=b'wonderful_picture'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 4, 50, 47, 857368)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 4, 50, 47, 856660)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='image',
            field=models.ImageField(upload_to=b'activity'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 4, 50, 47, 849635)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='image',
            field=models.ImageField(upload_to=b'xnews'),
        ),
    ]
