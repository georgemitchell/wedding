# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0005_auto_20170412_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
