# Django

## Shell命令
```BASH
    django-admin startproject 项目名字
    python manage.py startapp 应用名字
    
    # 启动服务
    python manage.py runserver
```

## 目录说明

    Projects
    │  db.sqlite3
    │  manage.py                        管理Django站点
    │
    ├─HelloDjango
    │      asgi.py
    │      settings.py                  项目配置文件
    │      urls.py                      URL路由配置
    │      wsgi.py                      内置runserver命令的WSGI应用配置
    │      __init__.py
    │
    ├─main                              应用目录
    │  │  admin.py                      网站后台管理
    │  │  apps.py
    │  │  models.py
    │  │  views.py                      接受请求、返回应答
    │  │  tests.py                      写测试代码的文件
    │  │  __init__.py
    │  │
    │  └─migrations
    │          __init__.py
    │
    └─templates