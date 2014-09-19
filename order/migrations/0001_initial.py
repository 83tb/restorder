# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import order.models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=255, blank=True)),
                ('label', models.CharField(max_length=255, blank=True)),
                ('mpoly', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('level2', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lamp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=255, blank=True)),
                ('mpoint', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_id', models.CharField(max_length=255, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('channel', models.CharField(max_length=255)),
                ('signature', models.CharField(max_length=255)),
                ('body', models.FileField(blank=True, upload_to=b'messages/%Y/%m/%d/', validators=[order.models.validate_file])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
