# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndInterface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 12, 15, 5, 51, 999031)),
        ),
        migrations.AlterField(
            model_name='information',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 12, 15, 5, 51, 997803)),
        ),
        migrations.AlterField(
            model_name='safeguard',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 12, 15, 5, 51, 999870)),
        ),
        migrations.AlterField(
            model_name='x_news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 12, 15, 5, 51, 996541)),
        ),
    ]
