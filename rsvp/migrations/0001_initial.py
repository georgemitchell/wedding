# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_code', models.CharField(max_length=8)),
                ('expires', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(unique=True, max_length=256, db_index=True)),
                ('num_guests_allowed', models.SmallIntegerField(default=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='guest',
            name='rsvp',
            field=models.ForeignKey(on_delete=models.CASCADE, to='rsvp.RSVP'),
        ),
        migrations.AddField(
            model_name='accesscode',
            name='rsvp',
            field=models.ForeignKey(on_delete=models.CASCADE, to='rsvp.RSVP'),
        ),
    ]
