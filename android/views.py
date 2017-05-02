# -*-coding:utf-8-*-
from django.db import connection
from django.http import request
from android import models
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def android_testcase(request):
    if request.GET.get('table', ''):
        table = request.GET.get('table', '')
        sql = 'select case_id,case_name,activity,name,action,value,expected,actual,result,state from ' + table
    else:
        table = 'a_login'
        sql = 'select case_id,case_name,activity,name,action,value,expected,actual,result,state from a_login'

    list = []
    sql2 = "select * from index_table where index_id = 0"
    cursor = connection.cursor()
    cursor.execute(sql, None)
    cursor2 = connection.cursor()
    cursor2.execute(sql2, None)
    col_names = [desc[0] for desc in cursor2.description]
    # print col_names
    caselist = cursor.fetchall()
    # table_list = cursor2.fetchall()
    for row in cursor2.fetchall():
        # row=cursor2.fetchall()
        list.append(dict(zip(col_names, row)))
    # print list
    # print table_list
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

    return render_to_response('android_testcase.html', {'testcase_list': contacts, 'table_list': list, 'table': table})
