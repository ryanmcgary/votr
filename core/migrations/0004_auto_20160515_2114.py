# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_voter_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='longitude',
            field=models.FloatField(),
        ),
    ]