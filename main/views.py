# 模板使用
from django.shortcuts import render

# 基础响应、请求
from django.http import HttpRequest, HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.sessions.backends.db import SessionStore
import json


def get_current_time_string():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


# Create your views here.
def first(request):
    """
    请求与响应
    """
    def get_request_message(_request):
        _message = {
            'http': {
                'HTTPS': _request.is_secure(),
                'AJAX': _request.is_ajax(),
                'METHOD': _request.method,
                'URI': _request.get_raw_uri(),
                'HOST':  _request.get_host(),
                'PORT':  _request.get_port(),
                'PATH': _request.path,
                'ENCODING': _request.encoding,
                'CONTENT_LENGTH': _request.META['CONTENT_LENGTH'],
                'CONTENT_TYPE': _request.META['CONTENT_TYPE'],
                'REMOTE_ADDR': _request.META['REMOTE_ADDR'],
            },
            'headers': _request.headers._store,     # _store is dict()
            'cookies': _request.COOKIES,            # COOKIES is dict()
            # from django.contrib.sessions.backends.db import SessionStore
            'session': _request.session._session,
            #  _request.GET, _request.POST is dict()
            'parameter': _request.GET if 'GET' == _request.method else _request.POST,
            'files': _request.FILES,                # FILES is dict()
        }
        return _message
    # end def
    print(type(request))
    request_message = get_request_message(request)

    # Session
    # request.session.clear()
    login_time = request.session.get('first_login_time', 'first')
    if login_time == 'first':
        request.session['first_login_time'] = get_current_time_string()
    request_message['first_login_time'] = login_time

    # Response
    response = HttpResponse()
    response.charset = 'utf-8'
    response.status_code = 200
    response['Content-Type'] = 'text/json'

    # Cookie
    # 注意set_cookie的其它参数
    response.set_cookie('last', get_current_time_string())

    response.write(json.dumps(request_message))
    return response


def second(request):
    """
    模板使用
    """
    return render(request, '../templates/main/index.html', {
        'title': '标题',
        'headline': '模板使用Demo',
        'range1': list(range(10)),
        'dict1': {'a': 'Apple', 'b': 'Banana', 2: '200'}
    })


def third(request):
    import random
    from main.models import Student

    # 添加数据
    stu = Student()
    stu.name = "名字"
    stu.number = random.randint(1000, 9999)
    stu.birthday = '1998-8-23'
    stu.is_del = False
    stu.save()

    # 查询数据
    print(Student.objects.all())
    stu = Student.objects.get(id=1)
    print(stu)
    # stu = Student.objects.filter(id=1)
    # print(stu)
    # stu = Student.objects.exclude(id=1)
    # print(stu)
    # print(Student.computer_set.all())

    # 修改数据
    stu.name = "修改"
    stu.save()

    # 删除数据
    # stu.delete()
    return HttpResponse("Success!")
