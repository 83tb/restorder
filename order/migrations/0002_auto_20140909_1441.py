# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='body',
            field=models.FileField(blank=True, upload_to=b'messages/%Y/%m/%d/', validators=[order.models.validate_file]),
        ),
    ]
