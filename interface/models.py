#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


REQUEST_LIST = (
        ('get','get'),
        ('post','post'),
        ('put','put'),
        ('patch','patch'),
        ('delete','delete'),
        )
# Create your models here.
class InterfaceTestcase1(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(max_length=45,unique=True)
    case_name = models.CharField(max_length=45)
    request_type = models.CharField(max_length=10,choices=REQUEST_LIST)
    url = models.CharField(max_length=100)
    parameters = models.TextField(null=True,blank=True,editable=False)
    body = models.TextField(null=True,blank=True)
    response = models.TextField(null=True,blank=True,editable=True)
    status_code = models.CharField(max_length=5,null=True,blank=True,editable=False)
    expected = models.TextField(null=True,blank=True)
    not_expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True,blank=True,editable=False)
    config = models.CharField(max_length=200,null=True,blank=True)
    result = models.CharField(max_length=5,null=True,blank=True,editable=False)
    time = models.IntegerField(null=True,blank=True,editable=False)
    state = models.IntegerField(default='1')
    datetime = models.DateTimeField(null=True,editable=False,default=None)

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = '微爱接口测试用例'
        verbose_name_plural = '微爱接口测试用例'
        # app_label = '接口测试'
        ordering = ['case_id']
        db_table = 'interface_love'

class InterfaceTestcase2(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(max_length=45,unique=True)
    case_name = models.CharField(max_length=45)
    request_type = models.CharField(max_length=10,choices=REQUEST_LIST)
    url = models.CharField(max_length=100)
    parameters = models.TextField(null=True,blank=True,editable=False)
    body = models.TextField(null=True,blank=True)
    response = models.TextField(null=True,blank=True,editable=True)
    status_code = models.CharField(max_length=5,null=True,blank=True,editable=False)
    expected = models.TextField(null=True,blank=True)
    not_expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True,blank=True,editable=False)
    config = models.CharField(max_length=200,null=True,blank=True)
    result = models.CharField(max_length=5,null=True,blank=True,editable=False)
    time = models.IntegerField(null=True,blank=True,editable=False)
    state = models.IntegerField(default='1')
    datetime = models.DateTimeField(null=True,editable=False,default=None)

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = '梦想接口测试用例'
        verbose_name_plural = '梦想接口测试用例'
        # app_label = '接口测试'
        ordering = ['case_id']
        db_table = 'interface_dream'

class InterfaceTestcase3(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(max_length=45,unique=True)
    case_name = models.CharField(max_length=45)
    request_type = models.CharField(max_length=10,choices=REQUEST_LIST)
    url = models.CharField(max_length=100)
    parameters = models.TextField(null=True,blank=True,editable=False)
    body = models.TextField(null=True,blank=True)
    response = models.TextField(null=True,blank=True,editable=True)
    status_code = models.CharField(max_length=5,null=True,blank=True,editable=False)
    expected = models.TextField(null=True,blank=True)
    not_expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True,blank=True,editable=False)
    config = models.CharField(max_length=200,null=True,blank=True)
    result = models.CharField(max_length=5,null=True,blank=True,editable=False)
    time = models.IntegerField(null=True,blank=True,editable=False)
    state = models.IntegerField(default='1')
    datetime = models.DateTimeField(null=True,editable=False,default=None)

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = '预售接口测试用例'
        verbose_name_plural = '预售接口测试用例'
        # app_label = '接口测试'
        ordering = ['case_id']
        db_table = 'interface_sale'

class InterfaceTestcase4(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(max_length=45,unique=True)
    case_name = models.CharField(max_length=45)
    request_type = models.CharField(max_length=10,choices=REQUEST_LIST)
    url = models.CharField(max_length=100)
    parameters = models.TextField(null=True,blank=True,editable=False)
    body = models.TextField(null=True,blank=True)
    response = models.TextField(null=True,blank=True,editable=True)
    status_code = models.CharField(max_length=5,null=True,blank=True,editable=False)
    expected = models.TextField(null=True,blank=True)
    not_expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True,blank=True,editable=False)
    config = models.CharField(max_length=200,null=True,blank=True)
    result = models.CharField(max_length=5,null=True,blank=True,editable=False)
    time = models.IntegerField(null=True,blank=True,editable=False)
    state = models.IntegerField(default='1')
    datetime = models.DateTimeField(null=True,editable=False,default=None)

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = '微爱接口测试用例(新)'
        verbose_name_plural = '微爱接口测试用例(新)'
        # app_label = '接口测试'
        ordering = ['case_id']
        db_table = 'interface_love_new'

class InterfaceConfig(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    name = models.CharField(max_length=45)
    value = models.CharField(max_length=300)
    state = models.IntegerField(default='1')
    models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '接口参数配置'
        verbose_name_plural = '接口参数配置'
        ordering = ['id']
        db_table = 'interface_config'

class InterfaceRecord(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    case_name = models.CharField(max_length=45,editable=False)
    time = models.IntegerField(null=True,blank=True,editable=False)
    status_code = models.CharField(max_length=5,null=True,blank=True,editable=False)
    datetime = models.DateTimeField(null=True,editable=False,default=None)

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = '接口请求历史记录'
        verbose_name_plural = '接口请求历史记录'
        ordering = ['id']
        db_table = 'interface_record'

