# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20170410_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotAttending',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='rsvp',
            name='telephone',
            field=models.CharField(max_length=16, blank=True),
        ),
        migrations.AddField(
            model_name='notattending',
            name='rsvp',
            field=models.ForeignKey(on_delete=models.CASCADE, to='rsvp.RSVP'),
        ),
    ]
