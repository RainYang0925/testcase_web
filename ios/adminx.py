import xadmin
from ios.models import *
# Register your models here.
class IOSTestCaseAdmin(object):
    list_display = ('case_id', 'case_name', 'page', 'name', 'action','value',
                    'expected','actual', 'result', 'state')
    search_fields = ('case_id', 'case_name', 'page', 'name', 'action', 'value',
                    'expected','actual', 'result', 'state')


xadmin.site.register(IOSTestCase1, IOSTestCaseAdmin)
xadmin.site.register(IOSTestCase2, IOSTestCaseAdmin)
xadmin.site.register(IOSTestCase3, IOSTestCaseAdmin)
xadmin.site.register(IOSTestCase4, IOSTestCaseAdmin)
xadmin.site.register(IOSTestCase5, IOSTestCaseAdmin)
xadmin.site.register(IOSTestCase6, IOSTestCaseAdmin)
xadmin.site.register(IOSTestCase7, IOSTestCaseAdmin)
# xadmin.site.register(IOSTestCase8, IOSTestCase8Admin)
xadmin.site.register(IOSTestCase9, IOSTestCaseAdmin)
xadmin.site.register(IOSTestCase10, IOSTestCaseAdmin)
xadmin.site.register(IOSTestCase11, IOSTestCaseAdmin)
# xadmin.site.register(IOSTestCase12, IOSTestCase12Admin)
# xadmin.site.register(IOSTestCase13, IOSTestCase13Admin)


