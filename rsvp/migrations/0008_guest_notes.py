# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0007_notattending_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
