# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 23:09
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muss', '0013_auto_20171007_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='users_likes',
        ),
        migrations.AddField(
            model_name='likecomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_comment', to='muss.Comment'),
        ),
    ]