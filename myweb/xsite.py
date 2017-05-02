# -*- coding:utf-8 -*-
from xadmin import Settings
from xadmin.views.list import ListAdminView
from xadmin.views import CommAdminView
from xadmin.plugins.actions import BaseActionView,ActionPlugin
from django.http import HttpResponse, HttpResponseRedirect
class Base(Settings):
    enable_themes = True
    use_bootswatch = True
    # menu_style = 'default'
# class List(ListAdminView):
    # ListAdminView.list_per_page = 20

class GlobalSetting(CommAdminView):
    CommAdminView.site_title = u'自动化测试用例管理'
    CommAdminView.site_footer = u'轻松筹'

class Comm(Settings):
    menu_style = 'accordion'


