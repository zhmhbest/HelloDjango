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
