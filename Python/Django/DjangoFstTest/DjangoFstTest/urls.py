from django.conf.urls import include, url
from django.contrib import admin

from teacher import views as tv

urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoFstTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 视图函数名称只有名称，无括号和参数
    url(r'^normalmap/', tv.do_normalmap),

    # 尖号表示以后的内容开头的表达式
    # 圆括号表示的是一个参数，里面的内容作为参数传递给被调用的函数
    # 参数名称以问号加大写P开头，尖括号里面就是参数的名字
    # 尖括号后面表示正则，[0-9]表示内容仅能是由0-9的数字构成
    # 后面大括号表示出现的数字，此处4表示只能出现四个0-9的数字
    # [0,1][0-9]表示第一位数字0-1之间构成，第二位数字0-9之间构成
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.withparam),



]
