# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0007_auto_20170217_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='star',
            name='url',
        ),
        migrations.AddField(
            model_name='star',
            name='image',
            field=models.ImageField(default=None, upload_to=b'star'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 19, 58, 53, 828718)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 19, 58, 53, 827150)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 19, 58, 53, 826493)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 19, 58, 53, 829360)),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 19, 58, 53, 831484)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 19, 58, 53, 830747)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 19, 58, 53, 825254)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 19, 58, 53, 824517)),
        ),
    ]
