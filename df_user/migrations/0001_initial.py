# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=30)),
                ('upasswd', models.CharField(max_length=40)),
                ('uemail', models.CharField(default=b'', max_length=40)),
                ('uiphone', models.CharField(default=b'', max_length=20)),
                ('usite', models.CharField(default=b'', max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
