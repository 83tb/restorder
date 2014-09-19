# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20140909_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='level2',
            new_name='level',
        ),
        migrations.AlterField(
            model_name='msg',
            name='body',
            field=models.FileField(blank=True, upload_to=b'messages/%Y/%m/%d/', validators=[order.models.validate_file]),
        ),
    ]
