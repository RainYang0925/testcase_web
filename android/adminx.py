import xadmin
from android.models import *
# Register your models here.
class AndroidTestCaseAdmin(object):
    list_display = ('case_id', 'case_name', 'activity', 'name', 'action', 'value',
                    'expected','actual', 'result', 'state')
    search_fields = ('case_id', 'case_name', 'activity', 'name', 'action', 'value',
                    'expected','actual', 'result', 'state')

class Android_DeviceAdmin(object):
    list_display = ('name', 'deviceName', 'platformVersion','resolution','appiumPort','bootstrapPort','udid')
    search_fields = ('name', 'deviceName', 'platformVersion','resolution','appiumPort','bootstrapPort','udid')
    list_editable = ['name','deviceName','platformVersion','resolution','appiumPort','bootstrapPort','udid']

xadmin.site.register(AndroidTestCase1, AndroidTestCaseAdmin)
xadmin.site.register(AndroidTestCase2, AndroidTestCaseAdmin)
xadmin.site.register(AndroidTestCase3, AndroidTestCaseAdmin)
xadmin.site.register(AndroidTestCase4, AndroidTestCaseAdmin)
xadmin.site.register(AndroidTestCase5, AndroidTestCaseAdmin)
xadmin.site.register(AndroidTestCase6, AndroidTestCaseAdmin)
xadmin.site.register(AndroidTestCase7, AndroidTestCaseAdmin)
# xadmin.site.register(AndroidTestCase8, AndroidTestCase8Admin)
xadmin.site.register(AndroidTestCase9, AndroidTestCaseAdmin)
xadmin.site.register(AndroidTestCase10, AndroidTestCaseAdmin)
xadmin.site.register(AndroidTestCase11, AndroidTestCaseAdmin)
xadmin.site.register(AndroidTestCase12, AndroidTestCaseAdmin)
# xadmin.site.register(AndroidTestCase13, AndroidTestCase13Admin)
xadmin.site.register(Android_Device,Android_DeviceAdmin)
xadmin.site.register(Android_MQC,AndroidTestCaseAdmin)

