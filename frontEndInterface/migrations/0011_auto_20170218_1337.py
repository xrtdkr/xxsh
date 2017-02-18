# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0010_auto_20170218_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 13, 37, 12, 372466)),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image',
            field=models.ImageField(upload_to=b'static/xxsh/apply', blank=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(default=None, upload_to=b'static/xxsh/carousel'),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 13, 37, 12, 370916)),
        ),
        migrations.AlterField(
            model_name='information',
            name='image',
            field=models.ImageField(default=None, upload_to=b'static/xxsh/information'),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 13, 37, 12, 370231)),
        ),
        migrations.AlterField(
            model_name='s_news',
            name='image',
            field=models.ImageField(upload_to=b'static/xxsh/snews'),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 13, 37, 12, 373056)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(upload_to=b'static/xxsh/staff'),
        ),
        migrations.AlterField(
            model_name='star',
            name='image',
            field=models.ImageField(default=None, upload_to=b'static/xxsh/star'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='image',
            field=models.ImageField(upload_to=b'static/xxsh/wonderful_picture'),
        ),
        migrations.AlterField(
            model_name='wondpicture',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 13, 37, 12, 375111)),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='compress_image',
            field=models.ImageField(default=None, upload_to=b'static/xxsh/wonderful_video'),
        ),
        migrations.AlterField(
            model_name='wondvideo',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 13, 37, 12, 374453)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 13, 37, 12, 368944)),
        ),
        migrations.AlterField(
            model_name='x_activity',
            name='image',
            field=models.ImageField(upload_to=b'static/xxsh/activity'),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 13, 37, 12, 368140)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='image',
            field=models.ImageField(upload_to=b'static/xxsh/xnews'),
        ),
    ]
