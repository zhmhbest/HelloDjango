# 模板使用
from django.shortcuts import render

# 基础响应、请求
from django.http import HttpRequest, HttpResponse
import json


# Create your views here.
def first(request):
    """
    请求与响应
    """
    def get_request_message(request):
        message = {
            'type': {
                'https': request.is_secure(),
                'ajax': request.is_ajax(),
            },
            'path': request.path,
            'headers': request.headers._store,
            'cookies': request.COOKIES,
            'encoding': request.encoding,
        }
        tmp_g = request.GET
        tmp_p = request.POST
        if 0 == len(tmp_g):
            message['parameter'] = tmp_p
        else:
            message['parameter'] = tmp_g
        # end if
        return message
    # end def
    response = HttpResponse()
    response.charset = 'utf-8'
    response.status_code = 200
    response['Content-Type'] = 'text/json'
    # response.set_cookie()
    request_message = get_request_message(request)
    response.write(json.dumps(request_message))
    return response


def second(request):
    """
    模板使用
    """
    return render(request, '../templates/main/index.html', {
        'title': '标题',
        'headline': '模板使用Demo',
        'range': list(range(10))
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
    # print(Student.computer_set.all())

    # 修改数据
    stu.name = "修改"
    stu.save()

    # 删除数据
    # stu.delete()
    return HttpResponse("Success!")
