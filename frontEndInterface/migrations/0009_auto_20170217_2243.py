# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0008_auto_20170217_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 22, 43, 38, 800317)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 22, 43, 38, 798761)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 22, 43, 38, 797858)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 22, 43, 38, 800977)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 22, 43, 38, 803136)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='compress_image',
            field=models.ImageField(default=None, upload_to=b'wonderful_video'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 22, 43, 38, 802464)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 22, 43, 38, 796615)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 22, 43, 38, 795806)),
        ),
    ]
