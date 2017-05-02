# __author__ = 'zzy'
#-*-coding:utf-8-*-

import pymysql

# =========设置连接测试是数据库========
host = '172.16.10.83'
user = 'root'
password = '12345678'
db = 'myweb'

# =========Mysql操作===============
class MySQLOperating(object):
    def __init__(self):
        try:
            #Connect to the database
            self.connection = pymysql.connect(host = host,
                                              user = user,
                                              password = password,
                                              db = db,
                                              charset = 'utf8mb4',
                                              cursorclass = pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print 'Mysql Error %d: %s' % (e.args[0],e.args[1])

    #向数据库中插入数据
    def insert(self, table_name, data):
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value +")"


        with self.connection:
            cur = self.connection.cursor()
            try:
                cur.execute(sql)
                # print 'execute sql success'
            # except:
            #     print 'execute sql fail'
            except pymysql.err.OperationalError as e:
                print 'Mysql Error %d: %s' % (e.args[0], e.args[1])

    #测试用例执行结果、接口返回数据、接口返回时间数据写入数据库:
    def set_InterfaceTableValue(self,table,case_id,key,value):
        sql = '''UPDATE %s SET %s = '%s' WHERE case_id = '%s' ''' %(table,key,value,case_id)
        with self.connection:
            cur = self.connection.cursor()
            cur.execute('SET NAMES utf8mb4;')
            try:
                # print sql
                cur.execute(sql)
                # print 'execute sql success'
            except pymysql.err.InternalError as e:
                print 'Mysql Error %d: %s' % (e.args[0], e.args[1])

    #接口返回数据作为引用参数写入数据库,如:torken,id
    def set_ConfigTableValue(self,key,value,state=1):
        if self.get_ConfigTableValue(key) == None:
            sql = "INSERT INTO interface_config (name,value,state) VALUES ('%s','%s','%s')" %(key, value ,state)
            # print '新增引用参数'
        else:
            sql = "UPDATE interface_config SET value = '%s' WHERE name = '%s'" %(value, key)
            # print sql
            # print '更新引用参数'
        with self.connection:
            cur = self.connection.cursor()
            try:
                # print sql
                cur.execute(sql)
                # print 'execute sql success'
            except pymysql.err.InternalError as e:
                print 'Mysql Error %d: %s' % (e.args[0], e.args[1])

    #获取数据库对应表中的所有测试用例,返回list
    def get_caselist(self,table_name):
        sql = "SELECT case_id,case_name,request_type,url,parameters,body,expected,not_expected,actual,config,state FROM %s"  % table_name
        with self.connection:
            cur = self.connection.cursor()
            try:
                cur.execute(sql)
                testcases_list = cur.fetchall()
                return testcases_list
            except:
                print 'get case error'
                return None
    #获取接口返回的引用参数
    def get_ConfigTableValue(self,key):
        sql = "SELECT value FROM interface_config WHERE name = '%s'" % key
        with self.connection:
            cur = self.connection.cursor()
            try:
                cur.execute(sql)
                value = cur.fetchone()
                # print 'execute sql success'
                if value == None:
                    return None
                else:
                    return value['value']
            except pymysql.err.InternalError as e:
                print 'Mysql Error %d: %s' % (e.args[0], e.args[1])

    def get_InterfaceTableValue(self, case_id, key):
        sql = "SELECT %s FROM interface_test1 WHERE case_id = '%s'" %(key,case_id)
        with self.connection:
            cur = self.connection.cursor()
            try:
                cur.execute(sql)
                value = cur.fetchone()
                print 'execute sql success'
                return value
            except pymysql.err.InternalError as e:
                print 'Mysql Error %d: %s' % (e.args[0], e.args[1])


if __name__ == '__main__':
    db = MySQLOperating()
    # db.set_InterfaceTableValue('test_1','paraeters',0)
    # testcaselist = db.get_caselist('interface_test')
    # for testcasedict in testcaselist:
    #     # print testcasedict
    #     for key in testcasedict:
    #         print '%s:%s' %(key,testcasedict[key])
    #     print '=' * 20
    print db.get_InterfaceTableValue('test_1','body')
    # db.set_ConfigTableValue('[access_token]','1111')
    print db.get_ConfigTableValue('[access_token]')