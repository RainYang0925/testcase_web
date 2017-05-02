#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

'''{'动物保护项目发布': 'i_animal_project_released',
            '灾难救助项目发布': 'i_disaster_project_released',
            '梦想清单项目发布': 'i_dream_project_released',
            '大病救助项目发布': 'i_illness_project_released',
            '扶贫助学项目发布': 'i_poverty_project_released',
            '尝鲜预售项目发布': 'i_presale_project_released',
            '支持已创建的项目': 'i_support_project',
            '其它项目发布': 'i_other_project_released',
            '个人中心': 'i_check_personal',
            '项目管理':'i_check_project',
            '查看个人项目发布':'i_check_build_project',
            '删除银行卡':'i_delete_card',
            '登录APP':'i_login',
            }
'''

class IOSTestCase1(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-动物保护项目发布'
        verbose_name_plural =  'IOS-动物保护项目发布'
        ordering = ['case_id']
        db_table = 'i_animal_project_released'

class IOSTestCase2(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-灾难救助项目发布'
        verbose_name_plural =  'IOS-灾难救助项目发布'
        ordering = ['case_id']
        db_table = 'i_disaster_project_released'

class IOSTestCase3(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-梦想清单项目发布'
        verbose_name_plural =  'IOS-梦想清单项目发布'
        ordering = ['case_id']
        db_table = 'i_dream_project_released'

class IOSTestCase4(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-大病救助项目发布'
        verbose_name_plural =  'IOS-大病救助项目发布'
        ordering = ['case_id']
        db_table = 'i_illness_project_released'

class IOSTestCase5(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-扶贫助学项目发布'
        verbose_name_plural =  'IOS-扶贫助学项目发布'
        ordering = ['case_id']
        db_table = 'i_poverty_project_released'

class IOSTestCase6(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-尝鲜预售项目发布'
        verbose_name_plural =  'IOS-尝鲜预售项目发布'
        ordering = ['case_id']
        db_table = 'i_presale_project_released'

class IOSTestCase7(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-其它项目发布'
        verbose_name_plural =  'IOS-其它项目发布'
        ordering = ['case_id']
        db_table = 'i_other_project_released'

class IOSTestCase8(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-支持已创建的项目'
        verbose_name_plural =  'IOS-支持已创建的项目'
        ordering = ['case_id']
        db_table = 'i_support_project'

class IOSTestCase9(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-个人中心'
        verbose_name_plural =  'IOS-个人中心'
        ordering = ['case_id']
        db_table = 'i_check_personal'

class IOSTestCase10(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-项目管理'
        verbose_name_plural =  'IOS-项目管理'
        ordering = ['case_id']
        db_table = 'i_check_project'

class IOSTestCase11(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-查看个人项目发布'
        verbose_name_plural =  'IOS-查看个人项目发布'
        ordering = ['case_id']
        db_table = 'i_check_build_project'

class IOSTestCase12(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-删除银行卡'
        verbose_name_plural =  'IOS-删除银行卡'
        ordering = ['case_id']
        db_table = 'i_delete_card'

class IOSTestCase13(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    case_id = models.CharField(unique=True, max_length=45)
    case_name = models.CharField(max_length=45)
    page = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    action = models.CharField(max_length=45, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)
    actual = models.TextField(null=True, blank=True, editable=False)
    result = models.CharField(max_length=5, null=True, blank=True, editable=False)
    state = models.IntegerField(default='1')

    def __unicode__(self):
        return self.case_name

    class Meta:
        verbose_name =  'IOS-登录APP'
        verbose_name_plural =  'IOS-登录APP'
        ordering = ['case_id']
        db_table = 'i_login'