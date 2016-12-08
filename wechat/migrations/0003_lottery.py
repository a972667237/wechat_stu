# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-08 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0002_auto_20161208_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openId', models.CharField(max_length=256, verbose_name='\u5fae\u4fe1\u8bc6\u522b\u7801')),
                ('lottery_id', models.CharField(max_length=16, verbose_name='\u62bd\u5956\u7f16\u53f7')),
                ('isUseful', models.BooleanField(default=False, verbose_name='\u662f\u5426\u6709\u6548')),
            ],
        ),
    ]