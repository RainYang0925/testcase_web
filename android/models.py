#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

'''{'动物保护项目发布': 'a_animal_project_released',
            '灾难救助项目发布': 'a_disaster_project_released',
            '梦想清单项目发布': 'a_dream_project_released',
            '大病救助项目发布': 'a_illness_project_released',
            '扶贫助学项目发布': 'a_poverty_project_released',
            '尝鲜预售项目发布': 'a_presale_project_released',
            '支持已创建的项目': 'a_support_project',
            '其它项目发布': 'a_other_project_released',
            '个人中心': 'a_check_my',
            '微爱大病救助项目管理':'a_check_illness',
            '尝鲜&梦想项目管理':'a_check_saledream',
            '微爱剩余项目管理':'a_check_love',
            '登录APP':'a_login',
            }
'''
ACTION_LIST = (('click','click'),
               ('sendkey','sendkey'),
               ('swipe','swipe'),
               ('tag','tag'),
               ('sleep','sleep'),
               ('back','back'),
               )
RESOLUTION_LIST = (('800x1280','800x1280'),
                   ('720x1280','720x1280'),
                   ('540x960','540x960'),
                   ('480x854','480x854'),
                   ('480x800','480x800'),
                   ('600x1024','600x1024'),
                   ('1200x1920','1200x1920'),
                   ('1080x1920','1080x1920'),
                   ('1080x1800','1080x1800'),
                   )

class AndroidTestCase1(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-动物保护项目发布'
		verbose_name_plural = 'Android-动物保护项目发布'
		ordering = ['case_id']
		db_table = 'a_animal_project_released'

class AndroidTestCase2(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-灾难救助项目发布'
		verbose_name_plural = 'Android-灾难救助项目发布'
		ordering = ['case_id']
		db_table = 'a_disaster_project_released'

class AndroidTestCase3(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-梦想清单项目发布'
		verbose_name_plural = 'Android-梦想清单项目发布'
		ordering = ['case_id']
		db_table = 'a_dream_project_released'

class AndroidTestCase4(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-大病救助项目发布'
		verbose_name_plural = 'Android-大病救助项目发布'
		ordering = ['case_id']
		db_table = 'a_illness_project_released'

class AndroidTestCase5(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-扶贫助学项目发布'
		verbose_name_plural = 'Android-扶贫助学项目发布'
		ordering = ['case_id']
		db_table = 'a_poverty_project_released'

class AndroidTestCase6(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-尝鲜预售项目发布'
		verbose_name_plural = 'Android-尝鲜预售项目发布'
		ordering = ['case_id']
		db_table = 'a_presale_project_released'

class AndroidTestCase7(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-其它项目发布'
		verbose_name_plural = 'Android-其它项目发布'
		ordering = ['case_id']
		db_table = 'a_other_project_released'

class AndroidTestCase8(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-支持已创建的项目'
		verbose_name_plural = 'Android-支持已创建的项目'
		ordering = ['case_id']
		db_table = 'a_support_project'

class AndroidTestCase9(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-个人中心'
		verbose_name_plural = 'Android-个人中心'
		ordering = ['case_id']
		db_table = 'a_check_my'

class AndroidTestCase10(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-微爱大病救助项目管理'
		verbose_name_plural = 'Android-微爱大病救助项目管理'
		ordering = ['case_id']
		db_table = 'a_check_illness'

class AndroidTestCase11(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-尝鲜&梦想项目管理'
		verbose_name_plural = 'Android-尝鲜&梦想项目管理'
		ordering = ['case_id']
		db_table = 'a_check_saledream'

class AndroidTestCase12(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-微爱剩余项目管理'
		verbose_name_plural = 'Android-微爱剩余项目管理'
		ordering = ['case_id']
		db_table = 'a_check_love'

class AndroidTestCase13(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')
	
	def __unicode__(self):
		return self.case_name
	
	class Meta:
		verbose_name = 'Android-登录APP'
		verbose_name_plural = 'Android-登录APP'
		ordering = ['case_id']
		db_table = 'a_login'

class Android_Device(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	name = models.CharField('设备名称', max_length=20, null=True, blank=True)
	deviceName = models.CharField('型号', max_length=20, null=True, blank=True)
	platformVersion = models.CharField('ANDROID版本', max_length=5, null=True, blank=True)
	resolution = models.CharField('分辨率', max_length=10, null=True, blank=True, choices=RESOLUTION_LIST)
	appiumPort = models.CharField('APPIUM端口', max_length=5, null=True, blank=True)
	bootstrapPort = models.CharField('BOOTSTRAP端口', max_length=5, null=True, blank=True)
	udid = models.CharField('UDID', max_length=20, null=True, blank=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Android-设备信息'
		verbose_name_plural = 'Android-设备信息'
		ordering = ['id']
		db_table = 'a_device'


class Android_MQC(models.Model):
	id = models.AutoField(primary_key=True, editable=False)
	case_id = models.CharField(max_length=45, unique=True)
	case_name = models.CharField(max_length=45)
	activity = models.CharField(max_length=60, null=True, blank=True)
	name = models.CharField(max_length=45, null=True, blank=True)
	action = models.CharField(max_length=10, null=True, blank=True, choices=ACTION_LIST)
	value = models.TextField(null=True, blank=True)
	expected = models.TextField(null=True, blank=True)
	actual = models.TextField(null=True, blank=True, editable=False)
	result = models.CharField(max_length=5, null=True, blank=True, editable=False)
	state = models.IntegerField(default='1')

	def __unicode__(self):
		return self.case_name

	class Meta:
		verbose_name = 'Android-MQC测试用例'
		verbose_name_plural = 'Android-MQC测试用例'
		ordering = ['case_id']
		db_table = 'a_mqc'
