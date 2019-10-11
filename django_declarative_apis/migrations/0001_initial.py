# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OauthConsumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(max_length=100, null=True)),
                ('key', models.CharField(db_index=True, max_length=18)),
                ('secret', models.CharField(max_length=32)),
                ('rsa_public_key_pem', models.TextField(blank=True, null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
