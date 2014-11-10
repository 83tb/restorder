# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20140909_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='level',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='msg',
            name='body',
            field=models.FileField(blank=True, upload_to=b'messages/%Y/%m/%d/', validators=[order.models.validate_file]),
        ),
    ]
