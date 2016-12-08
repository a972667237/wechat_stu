#coding=utf-8
from __future__ import unicode_literals

from django.db import models

REPLY_TYPE = (
    ('1', u'文字回复'),
    ('2', u'图文回复'),
)

# Create your models here.
class KeyWord(models.Model):
    keyword = models.CharField(
        '关键词', max_length=256, primary_key=True, help_text='用户发出的关键词')
    title = models.CharField('标题', max_length=256, null=True, blank=True)
    content = models.TextField(
        '内容', null=True, blank=True, help_text='回复给用户的内容')
    reply_type = models.CharField('回复类型', max_length=1, default="1", choices=REPLY_TYPE)
    to_url = models.URLField('跳转链接', null=True, blank=True)
    pic_url = models.URLField('图片链接', null=True, blank=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('发布状态', default=True)
 
    def __unicode__(self):
        return self.keyword
 
    class Meta:
        verbose_name='关键词'
        verbose_name_plural=verbose_name

class Wechat_settings(models.Model):
    access_token = models.CharField(max_length=256)
    access_token_expires_at = models.CharField(max_length=20)
    get_date = models.DateTimeField('更新时间', auto_now_add=True)
