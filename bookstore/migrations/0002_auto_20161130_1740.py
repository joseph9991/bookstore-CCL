# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='isbn13',
            field=models.ForeignKey(db_column='ISBN13', on_delete=django.db.models.deletion.DO_NOTHING, related_name='rate_isbn13_requests_created', to='bookstore.Book'),
        ),
    ]
