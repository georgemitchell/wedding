# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0006_rsvp_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='notattending',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
