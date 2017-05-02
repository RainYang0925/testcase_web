#-*-coding:utf-8-*-
from django.contrib import admin
import xadmin
from interface.models import *
from h5.models import *
from android.models import *
from pc.models import *
from ios.models import *
from xadmin.views import CommAdminView
from django.template import loader
from xadmin.sites import site
from xadmin.views import BaseAdminPlugin,ListAdminView
from xadmin.plugins.actions import BaseActionView
from django.http import HttpResponse,HttpResponseNotFound
from xadmin.util import lookup_field, label_for_field, force_unicode, json
from xadmin.plugins.utils import get_context_dict
from django.db import connection
from qsc_interfacetest.test_case.models.buildcase import BuildCase
from django.db import models
import chardet
import logging
import datetime
import decimal
import calendar
from django.utils.http import urlencode
from xadmin.views.dashboard import ModelBaseWidget, widget_manager
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import smart_unicode

try:
    import xlwt
    has_xlwt = True
except:
    has_xlwt = False

try:
    import xlsxwriter
    has_xlsxwriter = True
except:
    has_xlsxwriter = False

class ImportMenuPlugin(BaseAdminPlugin):
    list_export = ['csv']
    export_names = {'xlsx': 'Excel 2007', 'xls': 'Excel', 'csv': 'CSV',
                    'xml': 'XML', 'json': 'JSON'}

    def init_request(self, *args, **kwargs):
        self.list_export = [
            f for f in self.list_export
            if (f != 'xlsx' or has_xlsxwriter) and (f != 'xls' or has_xlwt)]
    # def init_request(self, *args, **kwargs):
    #     return self.request.GET.get('_do_') == 'import'

    def block_top_toolbar(self, context, nodes):
        if self.list_export:
            context.update({
                # 'show_export_all': self.admin_view.paginator.count > self.admin_view.list_per_page and not ALL_VAR in self.admin_view.request.GET,
                'form_params': self.admin_view.get_form_params({'_do_': 'import'}, ('import_type',)),
                'import_types': [{'type': et, 'name': self.export_names[et]} for et in self.list_export],
            })
            nodes.append(loader.render_to_string('model.top_toolbar.imports.html',
                                                context=get_context_dict(context)))

class ImportPlugin(BaseAdminPlugin):
    #导入插件定义
    table_list = {
        'h5testcase1':'h_animal_project_released',
        'h5testcase2':'h_disaster_project_released',
        'h5testcase3':'h_dream_project_released',
        'h5testcase4':'h_illness_project_released',
        'h5testcase5':'h_poverty_project_released',
        'h5testcase6':'h_presale_project_released',
        'h5testcase7':'h_other_project_released',
        'h5testcase8':'h_support_project',
        'h5testcase9':'h_check_my',
        'h5testcase10':'h_check_illness',
        'h5testcase11':'h_check_saledream',
        'h5testcase12':'h_check_love',
        'androidtestcase1':'a_animal_project_released',
        'androidtestcase2':'a_disaster_project_released',
        'androidtestcase3':'a_dream_project_released',
        'androidtestcase4':'a_illness_project_released',
        'androidtestcase5':'a_poverty_project_released',
        'androidtestcase6':'a_presale_project_released',
        'androidtestcase7':'a_other_project_released',
        'androidtestcase8':'a_support_project',
        'androidtestcase9':'a_check_my',
        'androidtestcase10':'a_check_illness',
        'androidtestcase11':'a_check_saledream',
        'androidtestcase12':'a_check_love',
        'androidtestcase13':'a_login',
        'iostestcase1':'i_animal_project_released',
        'iostestcase2':'i_disaster_project_released',
        'iostestcase3':'i_dream_project_released',
        'iostestcase4':'i_illness_project_released',
        'iostestcase5':'i_poverty_project_released',
        'iostestcase6':'i_presale_project_released',
        'iostestcase7':'i_other_project_released',
        'iostestcase8':'i_support_project',
        'iostestcase9':'i_check_personal',
        'iostestcase10':'i_check_project',
        'iostestcase11':'i_check_build_project',
        'iostestcase12':'i_delete_card',
        'iostestcase13':'i_login',
        'interfacetestcase1':'interface_test1',
        'interfaceconfig':'interface_config',
        'pctestcase1':'p_illness_project_released',
        'pctestcase2':'p_disaster_project_released',
        'pctestcase3':'p_animal_project_released',
        'pctestcase4':'p_poverty_project_released',
        'pctestcase5':'p_other_project_released',
        'pctestcase6':'p_presale_project_released',
        'pctestcase7':'p_dream_project_released',
    }

    #初始化插件
    def init_request(self, *args, **kwargs):
        # print self.request.Get.get('_do_')
        return True
    #获取post数据
    def post_response(self, *args, **kwargs):
        file = self.request.FILES.get('import_file','')
        if file:
            # table = self.request.META.get('PATH_INFO').split('/')[3]
            table = self.opts.db_table
            # print table
            self.message_user(self.set_db(file,table))
        else:
            pass
    #导入数据库数据
    def set_db(self,file,table):
        with open('/var/lib/mysql-files/testcase.csv','wb+') as testcase_file:
            for f in file.chunks():
                encode = chardet.detect(f)['encoding']
                testcase_file.write(f.decode(encode))
        with open('/var/lib/mysql-files/testcase.csv') as f_txt:
            column = (f_txt.readline().replace(' ','_')).replace('datetime','@datetime')
        sql = '''load data low_priority infile '/var/lib/mysql-files/testcase.csv' replace into table %s
                fields terminated by','
                enclosed by '"'
                lines terminated by'\r\n'
                ignore 1 lines
                (%s);
                '''%(table,column)
        try:
            cursor = connection.cursor()
            cursor.execute(sql, None)
            return u'数据导入完成！'
        except BaseException,e:
            return e

class RunAction(BaseActionView):

    action_name = "run_action"
    description = u'运行所选的 %(verbose_name_plural)s'
    model_perm = 'change'
    icon = 'fa fa-play-circle'

    def do_action(self, queryset):
        av = self.list_view
        table = self.opts.db_table
        for testcase in queryset.values():
            #执行接口测试用例
            try:
                result = BuildCase().execute_case(testcase,table)
                logging.info(result)
            except Exception,e:
                if len(queryset.values()) == 1:
                    av.message_user(e)
                else:
                    logging.error(e)
        msg = '运行完成！'
        av.message_user(msg)

@widget_manager.register
class MyChartWidget(ModelBaseWidget):
    widget_type = 'mchart'
    description = ('展示测试用例执行情况')
    template = 'xadmin/widgets/chart.html'
    widget_icon = 'fa fa-bar-chart-o'

    def convert(self, data):
        self.list_params = data.pop('params', {})
        self.chart = data.pop('chart', None)
    def setup(self):
        super(MyChartWidget, self).setup()

        self.charts = InterfaceRecordAdmin.data_mycharts

    def get_chart_url(self, name, v):
        return self.model_admin_url('mychart', name) + "?" + urlencode(self.list_params)

    def context(self, context):
        # print context
        context.update({
            'charts': [{"name": name, "title": v['title'], 'url': self.get_chart_url(name, v)} for name, v in self.charts.items()],
        })

    # Media
    def media(self):
        return self.vendor('flot.js', 'xadmin.plugin.charts.js')

class JSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return calendar.timegm(o.timetuple()) * 1000
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            try:
                return super(JSONEncoder, self).default(o)
            except Exception:
                return smart_unicode(o)

class MyChartsPlugin(BaseAdminPlugin):

    data_mycharts = {}

    def init_request(self, *args, **kwargs):
        return bool(self.data_mycharts)

    def get_chart_url(self, name, v):
        return self.admin_view.model_admin_url('mychart', name) + self.admin_view.get_query_string()

    # Media
    def get_media(self, media):
        return media + self.vendor('flot.js', 'xadmin.plugin.charts.js')

    # Block Views
    def block_results_top(self, context, nodes):
        context.update({
            'charts': [{"name": name, "title": v['title'], 'url': self.get_chart_url(name, v)} for name, v in self.data_mycharts.items()],
        })
        nodes.append(loader.render_to_string('model_list.results_top.charts.html', context_instance=context))

class MyChartsView(ListAdminView):

    data_mycharts = {}

    def get_ordering(self):
        if 'order' in self.chart:
            return self.chart['order']
        else:
            return super(MyChartsView, self).get_ordering()

    def get(self, request, name):
        # print request,name
        if name not in self.data_mycharts:
            return HttpResponseNotFound()

        self.chart = self.data_mycharts[name]

        self.x_field = self.chart['x-field']
        y_fields = self.chart['y-field']
        self.y_fields = (
            y_fields,) if type(y_fields) not in (list, tuple) else y_fields

        datas = [{"data":[], "label": force_unicode(label_for_field(
            i, self.model, model_admin=self))} for i in self.y_fields]
        self.make_result_list()
        result_list = self.get_list_queryset()._clone()
        for obj in result_list:
            # print obj.case_name
            if self.chart['title'] in obj.case_name :
                xf, attrs, value = lookup_field(self.x_field, obj, self)
                for i, yfname in enumerate(self.y_fields):
                    yf, yattrs, yv = lookup_field(yfname, obj, self)
                    datas[i]["data"].append((value, yv))

        option = {'series': {'lines': {'show': True}, 'points': {'show': False}},
                  'grid': {'hoverable': True, 'clickable': True}}
        try:
            xfield = self.opts.get_field(self.x_field)
            if type(xfield) in (models.DateTimeField, models.DateField, models.TimeField):
                option['xaxis'] = {'mode': "time", 'tickLength': 5}
                if type(xfield) is models.DateField:
                    option['xaxis']['timeformat'] = "%y/%m/%d"
                elif type(xfield) is models.TimeField:
                    option['xaxis']['timeformat'] = "%H:%M:%S"
                else:
                    option['xaxis']['timeformat'] = "%y/%m/%d %H:%M:%S"
        except Exception:
            pass

        option.update(self.chart.get('option', {}))
        # print datas
        content = {'data': datas, 'option': option}
        result = json.dumps(content, cls=JSONEncoder, ensure_ascii=False)
        # print result
        return HttpResponse(result)

site.register_plugin(ImportMenuPlugin,ListAdminView)
site.register_plugin(ImportPlugin,ListAdminView)
site.register_plugin(MyChartsPlugin, ListAdminView)
site.register_modelview(r'^mychart/(.+)/$', MyChartsView, name='%s_%s_mychart')



class InterfaceTestcaseAdmin(object):
    list_display = ('case_id','case_name','url','request_type','config','result','status_code','time','datetime')
    search_fields = ('case_id','case_name','url','request_type','result','state')
    list_editable = ['case_id','url','request_type','body']
    show_detail_fields = ['case_name']
    list_export = ['xls','json']
    actions = [RunAction, ]
    # data_mycharts = {
    #         "time_count": {'title': u"登录", "x-field": "datetime", "y-field": ('time','status_code'), "order": ('datetime',)},
    #          "state_count": {'title': u"接口数据返回状态表", "x-field": "case_id", "y-field": ('status_code',), "order": ('case_name',)}
    #     }
class InterfaceConfigAdmin(object):
    list_display = ('name','value','state')
    search_fields = ('name','value','state')
    list_editable = ['name','value','state']

class InterfaceRecordAdmin(object):
    search_fields = ('case_name')
    data_mycharts = {
            "login": {'title': u"登录", "x-field": "datetime", "y-field": ('time'), "order": ('datetime',)},
            "illness_released": {'title': u"发布大病项目", "x-field": "datetime", "y-field": ('time'), "order": ('datetime',)},
            "del": {'title': u"删除公益项目", "x-field": "datetime", "y-field": ('time'), "order": ('datetime',)},
        }

class GlobalSetting(object):
    #定义菜单
    def get_site_menu(self):
        return (
            {'title': '接口测试用例', 'perm': self.get_model_perm(InterfaceConfig, 'view'),
             'menus':(
                {'title':'微爱接口','url': self.get_model_url(InterfaceTestcase1, 'changelist')},
                {'title':'微爱接口(新)','url': self.get_model_url(InterfaceTestcase4, 'changelist')},
                {'title':'梦想接口','url': self.get_model_url(InterfaceTestcase2, 'changelist')},
                {'title':'预售接口','url': self.get_model_url(InterfaceTestcase3, 'changelist')},
                # {'title':'接口统计','url':self.get_model_url(InterfaceRecord, 'changelist')},
                {'title':'接口参数',  'url': self.get_model_url(InterfaceConfig, 'changelist')},
            )},
            {'title': 'H5测试用例', 'perm': self.get_model_perm(H5TestCase1, 'change'), 'menus': (
                {'title': '动物保护项目发布', 'url': self.get_model_url(H5TestCase1, 'changelist')},
                {'title': '灾难救助项目发布', 'url': self.get_model_url(H5TestCase2, 'changelist')},
                {'title': '梦想清单项目发布', 'url': self.get_model_url(H5TestCase3, 'changelist')},
                {'title': '大病救助项目发布', 'url': self.get_model_url(H5TestCase4, 'changelist')},
                {'title': '扶贫助学项目发布', 'url': self.get_model_url(H5TestCase5, 'changelist')},
                {'title': '尝鲜预售项目发布', 'url': self.get_model_url(H5TestCase6, 'changelist')},
                {'title': '其它项目发布', 'url': self.get_model_url(H5TestCase7, 'changelist')},
                # {'title': '支持已创建的项目', 'url': self.get_model_url(H5TestCase8, 'changelist')},
                {'title': '个人中心', 'url': self.get_model_url(H5TestCase9, 'changelist')},
                {'title': '微爱大病救助项目管理', 'url': self.get_model_url(H5TestCase10, 'changelist')},
                {'title': '尝鲜&梦想项目管理', 'url': self.get_model_url(H5TestCase11, 'changelist')},
                {'title': '微爱剩余项目管理', 'url': self.get_model_url(H5TestCase12, 'changelist')},
            )},
            {'title': 'Android测试用例', 'perm': self.get_model_perm(AndroidTestCase1, 'change'), 'menus': (
                {'title': '动物保护项目发布', 'url': self.get_model_url(AndroidTestCase1, 'changelist')},
                {'title': '灾难救助项目发布', 'url': self.get_model_url(AndroidTestCase2, 'changelist')},
                {'title': '梦想清单项目发布', 'url': self.get_model_url(AndroidTestCase3, 'changelist')},
                {'title': '大病救助项目发布', 'url': self.get_model_url(AndroidTestCase4, 'changelist')},
                {'title': '扶贫助学项目发布', 'url': self.get_model_url(AndroidTestCase5, 'changelist')},
                {'title': '尝鲜预售项目发布', 'url': self.get_model_url(AndroidTestCase6, 'changelist')},
                {'title': '其它项目发布', 'url': self.get_model_url(AndroidTestCase7, 'changelist')},
                # {'title': '支持已创建的项目', 'url': self.get_model_url(AndroidTestCase8, 'changelist')},
                {'title': '个人中心', 'url': self.get_model_url(AndroidTestCase9, 'changelist')},
                {'title': '微爱大病救助项目管理', 'url': self.get_model_url(AndroidTestCase10, 'changelist')},
                {'title': '尝鲜&梦想项目管理', 'url': self.get_model_url(AndroidTestCase11, 'changelist')},
                {'title': '微爱剩余项目管理', 'url': self.get_model_url(AndroidTestCase12, 'changelist')},
                # {'title': '登录APP', 'url': self.get_model_url(AndroidTestCase13, 'changelist')},
                {'title': '设备信息', 'url': self.get_model_url(Android_Device, 'changelist')},
                {'title': 'MQC测试用例', 'url': self.get_model_url(Android_MQC, 'changelist')},
            )},
            {'title': 'IOS测试用例', 'perm': self.get_model_perm(IOSTestCase1, 'change'), 'menus': (
                {'title': '动物保护项目发布', 'url': self.get_model_url(IOSTestCase1, 'changelist')},
                {'title': '灾难救助项目发布', 'url': self.get_model_url(IOSTestCase2, 'changelist')},
                {'title': '梦想清单项目发布', 'url': self.get_model_url(IOSTestCase3, 'changelist')},
                {'title': '大病救助项目发布', 'url': self.get_model_url(IOSTestCase4, 'changelist')},
                {'title': '扶贫助学项目发布', 'url': self.get_model_url(IOSTestCase5, 'changelist')},
                {'title': '尝鲜预售项目发布', 'url': self.get_model_url(IOSTestCase6, 'changelist')},
                {'title': '其它项目发布', 'url': self.get_model_url(IOSTestCase7, 'changelist')},
                # {'title': '支持已创建的项目', 'url': self.get_model_url(IOSTestCase8, 'changelist')},
                {'title': '个人中心', 'url': self.get_model_url(IOSTestCase9, 'changelist')},
                {'title': '项目管理', 'url': self.get_model_url(IOSTestCase10, 'changelist')},
                {'title': '查看个人项目发布', 'url': self.get_model_url(IOSTestCase11, 'changelist')},
                # {'title': '删除银行卡', 'url': self.get_model_url(IOSTestCase12, 'changelist')},
                # {'title': '登录APP', 'url': self.get_model_url(IOSTestCase13, 'changelist')},
            )},
            {'title': 'PC测试用例', 'perm': self.get_model_perm(PCTestCase1, 'change'), 'menus': (
                {'title': '大病救助项目发布', 'url': self.get_model_url(PCTestCase1, 'changelist')},
                {'title': '灾难救助项目发布', 'url': self.get_model_url(PCTestCase2, 'changelist')},
                {'title': '动物保护项目发布', 'url': self.get_model_url(PCTestCase3, 'changelist')},
                {'title': '扶贫助学项目发布', 'url': self.get_model_url(PCTestCase4, 'changelist')},
                {'title': '其他项目发布', 'url': self.get_model_url(PCTestCase5, 'changelist')},
                {'title': '尝鲜预售项目发布', 'url': self.get_model_url(PCTestCase6, 'changelist')},
                {'title': '梦想清单项目发布', 'url': self.get_model_url(PCTestCase7, 'changelist')},
                # {'title': '支持已创建的项目', 'url': self.get_model_url(H5TestCase8, 'changelist')},
                # {'title': '查看个人项目', 'url': self.get_model_url(H5TestCase9, 'changelist')},
            )},
        )


xadmin.site.register(CommAdminView,GlobalSetting)
xadmin.site.register(InterfaceTestcase1, InterfaceTestcaseAdmin)
xadmin.site.register(InterfaceTestcase2, InterfaceTestcaseAdmin)
xadmin.site.register(InterfaceTestcase3, InterfaceTestcaseAdmin)
xadmin.site.register(InterfaceTestcase4, InterfaceTestcaseAdmin)
xadmin.site.register(InterfaceRecord,InterfaceRecordAdmin)
xadmin.site.register(InterfaceConfig, InterfaceConfigAdmin)
