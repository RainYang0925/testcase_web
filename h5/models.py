#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

'''{'动物保护项目发布': 'h_animal_project_released',
            '灾难救助项目发布': 'h_disaster_project_released',
            '梦想清单项目发布': 'h_dream_project_released',
            '大病救助项目发布': 'h_illness_project_released',
            '扶贫助学项目发布': 'h_poverty_project_released',
            '尝鲜预售项目发布': 'h_presale_project_released',
            '其它项目发布': 'h_other_project_released',
            '支持已创建的项目': 'h_support_project',
            '查看个人项目':'h_check_project',
            '个人中心': 'h_check_my',
            '微爱大病救助项目管理':'h_check_illness',
            '尝鲜&梦想项目管理':'h_check_saledream',
            '微爱剩余项目管理':'h_check_love',
            }
'''
ACTION_LIST = (('click',u'click'),
               ('sendkey',u'sendkey'),
               ('sendkeys',u'sendkeys'),
               ('scroll',u'scroll'),
               ('swipe',u'swipe'),
               ('sleep',u'sleep'),
               ('back',u'back'),
               )
class H5TestCase1(models.Model):
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
        verbose_name = 'H5-动物保护项目发布'
        verbose_name_plural = 'H5-动物保护项目发布'
        ordering = ['case_id']
        db_table = 'h_animal_project_released'

class H5TestCase2(models.Model):
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
        verbose_name = 'H5-灾难救助项目发布'
        verbose_name_plural = 'H5-灾难救助项目发布'
        ordering = ['case_id']
        db_table = 'h_disaster_project_released'

class H5TestCase3(models.Model):
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
        verbose_name = 'H5-梦想清单项目发布'
        verbose_name_plural = 'H5-梦想清单项目发布'
        ordering = ['case_id']
        db_table = 'h_dream_project_released'

class H5TestCase4(models.Model):
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
        verbose_name = 'H5-大病救助项目发布'
        verbose_name_plural = 'H5-大病救助项目发布'
        ordering = ['case_id']
        db_table = 'h_illness_project_released'

class H5TestCase5(models.Model):
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
        verbose_name = 'H5-扶贫助学项目发布'
        verbose_name_plural = 'H5-扶贫助学项目发布'
        ordering = ['case_id']
        db_table = 'h_poverty_project_released'

class H5TestCase6(models.Model):
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
        verbose_name = 'H5-尝鲜预售项目发布'
        verbose_name_plural = 'H5-尝鲜预售项目发布'
        ordering = ['case_id']
        db_table = 'h_presale_project_released'

class H5TestCase7(models.Model):
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
        verbose_name = 'H5-其它项目发布'
        verbose_name_plural = 'H5-其它项目发布'
        ordering = ['case_id']
        db_table = 'h_other_project_released'

class H5TestCase8(models.Model):
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
        verbose_name = 'H5-支持已创建的项目'
        verbose_name_plural = 'H5-支持已创建的项目'
        ordering = ['case_id']
        db_table = 'h_support_project'

class H5TestCase9(models.Model):
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
        verbose_name = 'H5-查看个人项目'
        verbose_name_plural = 'H5-查看个人项目'
        ordering = ['case_id']
        db_table = 'h_check_my'

class H5TestCase10(models.Model):
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
        verbose_name = 'H5-微爱大病救助项目管理'
        verbose_name_plural = 'H5-微爱大病救助项目管理'
        ordering = ['case_id']
        db_table = 'h_check_illness'

class H5TestCase11(models.Model):
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
        verbose_name = 'H5-尝鲜&梦想项目管理'
        verbose_name_plural = 'H5-尝鲜&梦想项目管理'
        ordering = ['case_id']
        db_table = 'h_check_saledream'

class H5TestCase12(models.Model):
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
        verbose_name = 'H5-微爱剩余项目管理'
        verbose_name_plural = 'H5-微爱剩余项目管理'
        ordering = ['case_id']
        db_table = 'h_check_love'
