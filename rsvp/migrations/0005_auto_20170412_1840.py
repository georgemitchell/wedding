# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0004_accesscode_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesscode',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='meal',
            field=models.SmallIntegerField(choices=[(0, b"I don't care, surprise me!"), (1, b'Beef'), (2, b'Chicken'), (3, b'Vegetarian')]),
        ),
    ]
