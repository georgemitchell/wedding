# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_auto_20170411_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesscode',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 11, 6, 6, 48, 817721, tzinfo=utc), verbose_name=models.DateTimeField(auto_now_add=True)),
            preserve_default=False,
        ),
    ]
