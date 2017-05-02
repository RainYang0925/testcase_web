#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

'''{'动物保护项目发布': 'p_animal_project_released',
            '灾难救助项目发布': 'p_disaster_project_released',
            '梦想清单项目发布': 'p_dream_project_released',
            '大病救助项目发布': 'p_illness_project_released',
            '扶贫助学项目发布': 'p_poverty_project_released',
            '尝鲜预售项目发布': 'p_presale_project_released',
            '其它项目发布': 'p_other_project_released',
            }
'''
ACTION_LIST = (('click',u'点击'),
               ('sendkey',u'输入'),
               ('sendkeys',u'输入(不清除)'),
               ('scroll',u'滚动'),
               ('swipe',u'滑动'),
               ('sleep',u'等待'),
               ('back',u'返回'),
               )
class PCTestCase1(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    url = models.URLField(null=True,blank=True)
    name = models.CharField(max_length=45, null=True,blank=True)
    action = models.CharField(max_length=10, null=True,blank=True,choices=ACTION_LIST)
    value = models.TextField(null=True,blank=True)
    expected = models.TextField(null=True,blank=True)
    actual = models.TextField(null=True,blank=True, editable=False)
    result = models.CharField(max_length=5, null=True,blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = 'PC-大病救助项目发布'
        verbose_name_plural = 'PC-大病救助项目发布'
        ordering = ['case_id']
        db_table = 'p_illness_project_released'

class PCTestCase2(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    url = models.URLField(null=True,blank=True)
    name = models.CharField(max_length=45, null=True,blank=True)
    action = models.CharField(max_length=10, null=True,blank=True,choices=ACTION_LIST)
    value = models.TextField(null=True,blank=True)
    expected = models.TextField(null=True,blank=True)
    actual = models.TextField(null=True,blank=True, editable=False)
    result = models.CharField(max_length=5, null=True,blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = 'PC-灾难救助项目发布'
        verbose_name_plural = 'PC-灾难救助项目发布'
        ordering = ['case_id']
        db_table = 'p_disaster_project_released'

class PCTestCase3(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    url = models.URLField(null=True,blank=True)
    name = models.CharField(max_length=45, null=True,blank=True)
    action = models.CharField(max_length=10, null=True,blank=True,choices=ACTION_LIST)
    value = models.TextField(null=True,blank=True)
    expected = models.TextField(null=True,blank=True)
    actual = models.TextField(null=True,blank=True, editable=False)
    result = models.CharField(max_length=5, null=True,blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = 'PC-动物保护项目发布'
        verbose_name_plural = 'PC-动物保护项目发布'
        ordering = ['case_id']
        db_table = 'p_animal_project_released'

class PCTestCase4(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    url = models.URLField(null=True,blank=True)
    name = models.CharField(max_length=45, null=True,blank=True)
    action = models.CharField(max_length=10, null=True,blank=True,choices=ACTION_LIST)
    value = models.TextField(null=True,blank=True)
    expected = models.TextField(null=True,blank=True)
    actual = models.TextField(null=True,blank=True, editable=False)
    result = models.CharField(max_length=5, null=True,blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = 'PC-扶贫助学项目发布'
        verbose_name_plural = 'PC-扶贫助学项目发布'
        ordering = ['case_id']
        db_table = 'p_poverty_project_released'


class PCTestCase5(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    url = models.URLField(null=True,blank=True)
    name = models.CharField(max_length=45, null=True,blank=True)
    action = models.CharField(max_length=10, null=True,blank=True,choices=ACTION_LIST)
    value = models.TextField(null=True,blank=True)
    expected = models.TextField(null=True,blank=True)
    actual = models.TextField(null=True,blank=True, editable=False)
    result = models.CharField(max_length=5, null=True,blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = 'PC-其他项目发布'
        verbose_name_plural = 'PC-其它项目发布'
        ordering = ['case_id']
        db_table = 'p_other_project_released'


class PCTestCase6(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    url = models.URLField(null=True,blank=True)
    name = models.CharField(max_length=45, null=True,blank=True)
    action = models.CharField(max_length=10, null=True,blank=True,choices=ACTION_LIST)
    value = models.TextField(null=True,blank=True)
    expected = models.TextField(null=True,blank=True)
    actual = models.TextField(null=True,blank=True, editable=False)
    result = models.CharField(max_length=5, null=True,blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = 'PC-尝鲜预售项目发布'
        verbose_name_plural = 'PC-尝鲜预售项目发布'
        ordering = ['case_id']
        db_table = 'p_presale_project_released'

class PCTestCase7(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    url = models.URLField(null=True,blank=True)
    name = models.CharField(max_length=45, null=True,blank=True)
    action = models.CharField(max_length=10, null=True,blank=True,choices=ACTION_LIST)
    value = models.TextField(null=True,blank=True)
    expected = models.TextField(null=True,blank=True)
    actual = models.TextField(null=True,blank=True, editable=False)
    result = models.CharField(max_length=5, null=True,blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name = 'PC-梦想清单项目发布'
        verbose_name_plural = 'PC-梦想清单项目发布'
        ordering = ['case_id']
        db_table = 'p_dream_project_released'

