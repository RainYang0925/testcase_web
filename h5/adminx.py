#-*-coding:utf-8-*-
import xadmin
from xadmin.views import CommAdminView
from xadmin.plugins.actions import BaseActionView
from h5.models import *

# Register your models here.
class H5TestCaseAdmin(object):
    list_display = ('case_id', 'case_name', 'url', 'name', 'action','value',
                    'expected', 'actual', 'result', 'state')
    search_fields = ('case_id', 'case_name', 'url', 'name', 'action', 'value',
                    'expected', 'actual', 'result', 'state')
xadmin.site.register(H5TestCase1, H5TestCaseAdmin)
xadmin.site.register(H5TestCase2, H5TestCaseAdmin)
xadmin.site.register(H5TestCase3, H5TestCaseAdmin)
xadmin.site.register(H5TestCase4, H5TestCaseAdmin)
xadmin.site.register(H5TestCase5, H5TestCaseAdmin)
xadmin.site.register(H5TestCase6, H5TestCaseAdmin)
xadmin.site.register(H5TestCase7, H5TestCaseAdmin)
# xadmin.site.register(H5TestCase8, H5TestCase8Admin)
xadmin.site.register(H5TestCase9, H5TestCaseAdmin)
xadmin.site.register(H5TestCase10, H5TestCaseAdmin)
xadmin.site.register(H5TestCase11, H5TestCaseAdmin)
xadmin.site.register(H5TestCase12, H5TestCaseAdmin)





