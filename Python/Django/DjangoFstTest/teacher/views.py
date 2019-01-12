from django.shortcuts import render
from django.http import HttpResponse    #把views里的内容包装成http形式,发还给浏览器

# Create your views here.
'''
视图函数需要一个参数，类型应该是HttpRequest
'''

def do_normalmap(request):
    return HttpResponse("This is normalmap.")


def withparam(request, year, month):
    return HttpResponse("This is with param {0},{1}".format(year,month))