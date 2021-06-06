# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0008_guest_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='rsvp',
            field=models.ForeignKey(on_delete=models.CASCADE, related_name='guests', to='rsvp.RSVP'),
        ),
    ]
