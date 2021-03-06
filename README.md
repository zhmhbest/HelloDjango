# Django
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
&nbsp;<br><br><br>&nbsp;
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
## MVT
- M: 模型，对应MVC的M，用于与数据库交互。
- V: 视图，对应MVC的C，用于接受请求和响应数据。
- T: 模板，对应MVC的V，用于决定最终显示样式。
&nbsp;<br>&nbsp;
&nbsp;<br>&nbsp;
&nbsp;<br>&nbsp;
## manage.py
### 创建项目
```
django-admin startproject 项目名字
```
### 创建应用
```
python manage.py startapp 应用名字
```
### 启动服务
```
python manage.py runserver [ip:port]
```
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
&nbsp;<br><br><br>&nbsp;
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
## Index

    Projects
    │  db.sqlite3                       数据库文件
    │  manage.py                        管理Django站点
    │
    ├─HelloDjango                       <项目名称>
    │      asgi.py
    │      settings.py                  项目配置文件
    │      urls.py                      URL路由配置
    │      wsgi.py                      WSGI应用配置
    │      __init__.py
    │
    ├─main                              <应用名称>
    │  │  admin.py                      网站后台管理
    │  │  apps.py
    │  │  models.py                     数据库设计
    │  │  views.py                      接受请求、返回应答
    │  │  tests.py                      测试代码
    │  │  __init__.py
    │  │
    │  └─migrations                     迁移文件目录
    │          __init__.py
    │
    └─templates
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
&nbsp;<br><br><br>&nbsp;
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
## Settings
- [HelloDjango/settings.py](https://github.com/zhmhbest/HelloDjango/blob/master/HelloDjango/settings.py)
### 注册应用
```python
INSTALLED_APPS = [
    # 注册应用
    'main.apps.MainConfig', 
]
```

### 数据库配置
```python
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ...
# ...
# ...
DATABASES = {
    'default': {
        # 【sqlite】
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        
        # 【mysql】
        # pip install pymysql
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '${数据库名}',
        'USER': '${数据库登录用户名}',
        'PASSWORD': '${数据库登录密码}',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}
```
#### main/\_\_init\_\_.py
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### 语言本地化
```python
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
&nbsp;<br><br><br>&nbsp;
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
## 可视化后台管理
### 创建超级管理员
```
python manage.py createsuperuser
#   ...\python.exe manage.py c  reatesuperuser
#   用户名 (leave blank to use 'zhmhb'): zhmh
#   电子邮件地址: zhmhbest@gmail.com
#   Password: 1234
#   Password (again): 1234
#   密码长度太短。密码必须包含至少 8 个字符。
#   这个密码太常见了。
#   密码只包含数字。
#   Bypass password validation and create user anyway? [y/N]: y
#   Superuser created successfully.
```
### 登录管理界面
```
http://127.0.0.1:8000/admin/
```
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
&nbsp;<br><br><br>&nbsp;
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
## Module
### 设计数据库模型
- [main/models.py](https://github.com/zhmhbest/HelloDjango/blob/master/main/models.py)
### 迁移文件
#### 生成迁移文件
```
python manage.py makemigrations
#   Migrations for 'main':
#   main\migrations\0001_initial.py
#       - Create model Table
```
#### 执行迁移文件
```
python manage.py migrate
#   Operations to perform:
#       Apply all migrations: admin, auth, contenttypes, main, sessions
#   Running migrations:
#       Applying ...
#       Applying ...
#       ...
```
### 模型使用
- [main/views.py](https://github.com/zhmhbest/HelloDjango/blob/master/main/views.py)
### 注册模型到后台管理界面
- [main/admin.py](https://github.com/zhmhbest/HelloDjango/blob/master/main/admin.py)
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
&nbsp;<br><br><br>&nbsp;
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
## View
### 创建接口
- [main/views.py](https://github.com/zhmhbest/HelloDjango/blob/master/main/views.py)

### 路由配置
- [HelloDjango/urls.py](https://github.com/zhmhbest/HelloDjango/blob/master/HelloDjango/urls.py)
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
&nbsp;<br><br><br>&nbsp;
<!-- ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->
## Template
### 设置模板文件目录
- [HelloDjango/settings.py](https://github.com/zhmhbest/HelloDjango/blob/master/HelloDjango/settings.py)
### 使用模板
- [main/views.py](https://github.com/zhmhbest/HelloDjango/blob/master/main/views.py)
- [templates/main/index.html](https://github.com/zhmhbest/HelloDjango/blob/master/templates/main/index.html)
