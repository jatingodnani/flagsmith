# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0007_organisation_pending_cancellation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='free_to_use_subscription',
            field=models.BooleanField(default=True),
        ),
    ]