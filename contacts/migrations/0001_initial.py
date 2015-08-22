# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_phasedout_age', models.DateTimeField(default=datetime.datetime.now)),
                ('contact_name', models.CharField(max_length=64)),
                ('contact_ph_num', models.CharField(max_length=13)),
                ('contact_emailid', models.EmailField(max_length=100)),
                ('contact_last_contacted', models.IntegerField(default=1)),
            ],
        ),
    ]
