# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0001_initial'),
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trips',
            name='user_id',
        ),
        migrations.AddField(
            model_name='trips',
            name='plannedby_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='planner', to='loginreg.Users'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trips',
            name='user_joining_id',
            field=models.ManyToManyField(related_name='joining', to='loginreg.Users'),
        ),
    ]
