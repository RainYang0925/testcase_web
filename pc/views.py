#-*-coding:utf-8-*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pc_testcase(request):
    # print request.GET.get('table', '')
    if request.GET.get('table', ''):
        table = request.GET.get('table', '').split('-')[0]
        # print state,table
        sql = 'select case_id,case_name,url,name,action,value,expected,actual,result,state from ' + table
    else:
        table = 'p_illness_project_released'
        sql = 'select case_id,case_name,url,name,action,value,expected,actual,result,state from p_illness_project_released'

    list = []
    sql2 = "select * from index_table where index_id = 3"
    cursor = connection.cursor()
    cursor.execute(sql, None)
    cursor2 = connection.cursor()
    cursor2.execute(sql2, None)
    col_names = [desc[0] for desc in cursor2.description]
    # print col_names
    caselist = cursor.fetchall()
    # print caselist
    # table_list = cursor2.fetchall()
    #返回数据库index_table表的数据
    for row in cursor2.fetchall():
        # row=cursor2.fetchall()
        list.append(dict(zip(col_names, row)))
    # print list
    # print table_list
    # 对数据库中测试用例表进行分页查询
    paginator = Paginator(caselist, 15)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('pc_testcase.html', {'testcase_list': contacts, 'table_list': list, 'table': table})