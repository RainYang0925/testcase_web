# __author__ = 'zhanghzhiyuan'
# -*-coding:utf-8-*-


from qsc_interfacetest.db_fixture.mysql_setting import MySQLOperating
from myunit import MyTest
import unittest
import logging
import re
import requests
import json
import time
import urllib
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')
import os
'''
===========说明============
功能:测试用例执行
入口:ecxel表格测试用例
==========================
'''

class BuildCase(MyTest):
    '''测试用例基础类'''

    def __init__(self):
        unittest.TestCase.__init__(self, '__init__')
        self.db = MySQLOperating()
        # self.base_url = 'http://api.test.qschou.com/v5'
        self.path = os.path.dirname(__file__)
        self.log_txt = self.path.split('test_case')[0] + 'report/log/log.txt'   #配置日志文件位置
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename=self.log_txt,
                            filemode='w')
        self.response = {}  #接口返回数据经处理后的字典

    # 获取接口返回数据,将嵌套字典处理为普通字典返回
    def change_response(self,dic):
        for key in dic:
            if isinstance(dic[key], dict):
                self.change_response(dic[key])
            else:
                # print '%s:%s' % (key, dic[key])
                self.response[key]=dic[key]
        return self.response

    # 获取返回接口返回结果中的指定的数据,response为返回的数据,key为指定值得索引
    def compare_response(self,response, key):
        #定义列表用于存放参数列表
        config_list = []
        #判断是否存在多个config
        if ';' in key:
            for config in key.split(';'):
                # 定义字典用于存放参数名和值、索引
                config_dic = {}
                #判断是否自定义参数名
                if '=' in config:
                    config_dic['name'] = config.split('=')[0]
                    config = config.split('=')[1]
                else:
                    config_dic['name'] = config
                if '-' in config:
                    # 分离config和索引以'_'分隔
                    config_dic['config'] = config.split('-')[0]
                    config_dic['index'] = int(config.split('-')[1])
                    # 将字典加入到列表中
                    config_list.append(config_dic)
                else:
                    # 不存在索引默认为0
                    config_dic['config'] = config
                    config_dic['index'] = 0
                    #将字典加入到列表中
                    config_list.append(config_dic)
        # 判断congfig中是否包含索引
        elif '-' in key:
            config_dic = {}
            #判断是否要自定义命名提取参数
            if '=' in key:
                config_dic['name'] = key.split('=')[0]
                key = key.split('=')[1]
            else:
                config_dic['name'] = key
            config_dic['config'] = key.split('-')[0]
            config_dic['index'] = int(key.split('-')[1])
            config_list.append(config_dic)
        else:
            #判断是否要自定义命名提取参数
            if '=' in key:
                config_dic = {}
                #等号左边为写入数据库中key
                config_dic['name'] = key.split('=')[0]
                #等号右边为写入数据库中value
                config_dic['config'] = key.split('=')[1]
                config_dic['index'] = 0
                config_list.append(config_dic)
            else:
                config_dic = {}
                config_dic['name'] = key
                config_dic['config'] = key
                config_dic['index'] = 0
                config_list.append(config_dic)

        # 遍历匹配查找在response中的config
        for config_dict in config_list:
            str1 = ': "?([^,\"\}\]]+)[",}?]'  # 此规则针对字符串、null
            q = '"' + config_dict['config'] + '"' + str1
            value = re.compile(q)
            temp = value.findall(str(response))
            # print 'temp:'
            # print temp
            if temp != []:
                # 说明有取出，返回
                config_dict['value'] = temp[config_dict['index']]
                # print '获取response中的值->' + config_dict['name'] + ':' + config_dict['value']
            else:  # 换成数字匹配规则
                num1 = ": ([\d]+)"
                q = '"' + config_dict['config'] + '"' + num1
                value = re.compile(q)
                temp = value.findall(str(response))
                if temp != []:
                    # 说明有取出，返回
                    config_dict['value'] = temp[config_dict['index']]
                    # print '获取response中的值->'+ config_dict['name'] + ':' + config_dict['value']
                else:
                    config_dict['value'] = None  # 无取出
                    # print '获取response中的值->' + config_dict['name'] + ':' + str(config_dict['value'])
        # 返回参数列表 如:[{'index': 0, 'config': u'access_token', 'name': u'access_token', 'value': '*********'}]
        return config_list

    # 替换参数中包含${**}之中的值,从数据库获取
    def replace_config(self,config):
        # value = re.compile(r'%%([^,]+?)[,/\'\"]')
        value = re.compile(r'\$\{([^\}]+?)\}')
        # 从数据库中获取引用参数,传给body
        re_result = value.findall(config)
        # print u'查询config表中的参数值:'
        # print re_result
        for i in re_result:
            i_value = self.db.get_ConfigTableValue(i)
            # print i+":"+i_value
            config = config.replace('${'+ i + '}',i_value)
        return config


    # 接口测试结束,写入相关数据,如:返回代码,时间,返回数据
    def set_db(self,testcase,r,table):
        # 获取接口返回时间
        time = r.elapsed.microseconds / 1000

        # 获取请求返回数据
        self.code = r.status_code
        text = r.text

        # 定义错误代码列表
        expect = True
        error_code = ['400', '401', '403', '404', '405', '406', '412', '422', '500']

        # 判断接口返回的代码是否在错误代码列表中,如果在数据库写入fail,并且将返回的错误信息赋值给response
        if str(r.status_code) in error_code:
            response = json.loads(text)['error']
            expect = False
            self.db.set_InterfaceTableValue(table,testcase['case_id'], 'result', 'error')
        else:
            response = json.dumps(json.loads(text), ensure_ascii=False, encoding='utf8mb4',indent=1)

        # 将请求返回数据写入数据库
        # value = {'status_code':code,'response':response,'time':time,'datetime':self.datetime}
        # self.db.set_InterfaceTableValue(testcase['case_id'], value)
        self.db.set_InterfaceTableValue(table,testcase['case_id'], 'status_code', self.code)
        self.db.set_InterfaceTableValue(table,testcase['case_id'], 'response', response)
        self.db.set_InterfaceTableValue(table,testcase['case_id'], 'time', time)
        self.db.set_InterfaceTableValue(table,testcase['case_id'],'datetime',self.datetime)
        # print self.datetime
        # 如果用例中包含返回的数据用作之后用例的请求参数,则将参数写入config表中
        if testcase['config']:
            config_value = self.compare_response(str(response), testcase['config'])
            # 将查找到的config参数遍历写入数据库
            for config in config_value:
                self.db.set_ConfigTableValue(config['name'], config['value'])

        #断言判断接口返回代码是否为错误代码
        msg = self.url + '\n' + u'接口返回异常:'+ ' ' +str(self.code) + ' ' + response
        self.assertTrue(expect,msg)

    # 执行测试用例,接收一条测试用例(字典:testcase),数据库表名(tablename,目前默认数据库中的interface_test1表,所以不传参数)
    def execute_case(self,testcase,tablename):
        '''执行测试用例'''

        # -------------------------------------接口输入参数设置---------------------------------------
        # 判断该接口用例是否为登录接口,非登录接口headers中包含token
        if '登录' in testcase['case_name']:
            headers = eval(self.db.get_ConfigTableValue('headers'))
        else:
            headers = eval(self.db.get_ConfigTableValue('headers'))
            headers['Authorization'] = 'Bearer '+ self.db.get_ConfigTableValue('access_token')
            # print self.db.get_ConfigTableValue('access_token')

        # 判断url里面是否包含引用参数
        if "${" in testcase['url']:
            self.url = self.replace_config(testcase['url'])
        else:
            self.url = testcase['url']
        # 判断是否需要传入parameter
        if testcase['parameters']:
            # 判断是否包含引用参数
            if "${" in testcase['parameters']:
                parameters = self.replace_config(testcase['parameters'])
            else:
                parameters = testcase['parameters']
            path = urllib.urlencode(eval(parameters))
            uri = '?' + path
        else:
            uri = ''
        self.url = self.url + uri

        # 判断body里面是否有引用参数
        if testcase['body']:
            if '${' not in testcase['body']:
                body = testcase['body']
                # print body
            else:
                body = self.replace_config(testcase['body'])
                # print body
        #-------------------------------------执行测试用例---------------------------------------
        logging.info(u'==========开始执行测试用例' + testcase['case_id'] + '===========')
        # 格式化时间形式
        ISOTIMEFORMAT = "%Y-%m-%d %H:%M:%S"
        if testcase['request_type'] == 'get':
            # 获取发起请求时间
            self.datetime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            # 发起请求
            r = requests.get(self.url,headers=headers)
            # 结果写入数据库
            self.set_db(testcase,r,tablename)

        if testcase['request_type'] == 'post':
            # 获取发起请求时间
            self.datetime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            # 发起请求
            # r = requests.post(self.url, data=json.dumps(eval(body,{'false': False, 'true': True, 'null': None})), headers=headers)
            r = requests.post(self.url, data=json.dumps(eval(body)),headers=headers)
            # 结果写入数据库
            self.set_db(testcase,r,tablename)

        if testcase['request_type'] == 'put':
            # 获取发起请求时间
            self.datetime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            # 发起请求
            r = requests.put(self.url, data=json.dumps(eval(body)), headers=headers)
            # 结果写入数据库
            self.set_db(testcase,r,tablename)

        if testcase['request_type'] == 'patch':
            # 获取发起请求时间
            self.datetime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            # 发起请求
            r = requests.patch(self.url, data=json.dumps(eval(body)), headers=headers)
            # 结果写入数据库
            self.set_db(testcase,r,tablename)

        if testcase['request_type'] == 'delete':
            # 获取发起请求时间
            self.datetime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            # 发起请求
            r = requests.delete(self.url, headers=headers)
            # 结果写入数据库
            self.set_db(testcase,r,tablename)

        response = json.dumps(json.loads(r.text), ensure_ascii=False, encoding='utf-8')

        #--------------------------------------判断接口返回数据与预期比较------------------------------------------
        # print u'测试ID:%s,请求接口地址:%s,返回代码:%s,返回数据：%s' %(testcase['case_id'],self.url,r.status_code,response)
        # 判断预期结果
        if testcase['expected']:
            expected = eval(testcase['expected'],{'false': False, 'true': True, 'null': None})
            for key,value in expected.items():
                actual = self.compare_response(response,key)[0]['value']
                if actual != None:
                    self.assertTrue(actual,msg=u'接口返回数据异常')
                # 将字典中的null转化为'null'字符串,注:python中没有null,只有None
                if  actual == 'null':
                    actual = None
                if actual == 'true':
                    actual = True
                if actual == 'false':
                    actual = False
                # print u'接口返回数据',actual
                # print u'预期返回数据',value
                #判断预期结果是否有返回值
                if value != '$':
                    #判断预期结果与实际结果数据是否一致
                    if actual == value:
                        self.db.set_InterfaceTableValue(tablename,testcase['case_id'],'result','pass')
                        self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'actual', u'一致')
                    else:
                        self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'result', 'fail')
                        msg = u'''%s\n状态码:%s\n接口返回数据与预期返回数据不一致\n接口返回数据:%s\n预期返回数据:%s''' %(self.url,self.code,actual,value)
                        self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'actual', key+':'+str(value))
                        self.assertEqual(actual,value,msg)
                else:
                    if actual != None:
                        self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'result', 'pass')
                        self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'actual', u'一致')
                    else:
                        self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'result', 'fail')
                        msg = u'''%s\n接口预期结果%s未返回数据''' %(self.url,actual)
                        self.assertEqual(actual,value,msg)

        # 判断反预期结果
        if testcase['not_expected']:
            expected = eval(testcase['not_expected'], {'false': False, 'true': True, 'null': None})
            for key, value in expected.items():
                actual = self.compare_response(response, key)[0]['value']
                if actual != None:
                    self.assertTrue(actual, msg=u'接口返回数据异常')
                # 将字典中的null转化为'null'字符串,注:python中没有null,只有None
                if actual == 'null':
                    actual = None
                if actual == 'true':
                    actual = True
                if actual == 'false':
                    actual = False
                # print u'接口返回数据',actual
                # print u'预期返回数据',

                # 判断预期结果与实际结果数据是否一致
                if actual != value:
                    self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'result', 'pass')
                    self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'actual', u'一致')
                else:
                    self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'result', 'fail')
                    msg = u'''%s\n状态码:%s\n接口返回数据与预期返回数据不一致\n接口返回数据:%s\n预期不返回数据:%s''' % (
                    self.url,self.code,actual, value)
                    self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'actual',
                                                    key + ':' + str(value))
                    self.assertNotEqual(actual, value, msg)

            # print u'预期结果与实际结果一致'
        self.db.set_InterfaceTableValue(tablename,testcase['case_id'], 'result', 'pass')
        logging.info(u'==========测试用执行完成' + testcase['case_id'] + '===========\n\r')

if __name__ == '__main__':
    T = BuildCase()
