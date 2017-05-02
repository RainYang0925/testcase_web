import xadmin
from pc.models import *

# Register your models here.
class PCTestCaseAdmin(object):
    list_display = ('case_id', 'case_name', 'url', 'name', 'action','value',
                    'expected', 'actual', 'result', 'state')
    search_fields = ('case_id', 'case_name', 'url', 'name', 'action', 'value',
                    'expected', 'actual', 'result', 'state')

xadmin.site.register(PCTestCase1, PCTestCaseAdmin)
xadmin.site.register(PCTestCase2, PCTestCaseAdmin)
xadmin.site.register(PCTestCase3, PCTestCaseAdmin)
xadmin.site.register(PCTestCase4, PCTestCaseAdmin)
xadmin.site.register(PCTestCase5, PCTestCaseAdmin)
xadmin.site.register(PCTestCase6, PCTestCaseAdmin)
xadmin.site.register(PCTestCase7, PCTestCaseAdmin)




