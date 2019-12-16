# Django



## MVT
- M: 模型，对应MVC的M，用于与数据库交互。
- V: 视图，对应MVC的C，用于接受请求和响应数据。
- T: 模板，对应MVC的V，用于决定最终显示样式。



## 项目管理
### 创建项目
```BASH
django-admin startproject 项目名字
```
### 创建应用
```BASH
python manage.py startapp 应用名字
```
### 启动服务
```BASH
python manage.py runserver [ip:port]
```



## 目录说明

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



## 可视化后台管理
### 语言本地化
[HelloDjango/settings.py#105](https://github.com/zhmhbest/HelloDjango/blob/master/HelloDjango/settings.py#L105)
```PYTHON
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```
### 创建超级管理员
```BASH
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



## Module
### 设计模型
[main/models.py](https://github.com/zhmhbest/HelloDjango/blob/master/main/models.py)

### 迁移文件
#### 生成迁移文件
```BASH
python manage.py makemigrations
#   Migrations for 'main':
#   main\migrations\0001_initial.py
#       - Create model Table
```
#### 执行迁移文件
```BASH
python manage.py migrate
#   Operations to perform:
#       Apply all migrations: admin, auth, contenttypes, main, sessions
#   Running migrations:
#       Applying ...
#       Applying ...
#       ...
```

### 模型使用
#### 加入数据
```PYTHON
stu = Student()
stu.name = "名字"
stu.number = 20195532
stu.birthday = date(1998, 8, 23)
stu.is_del = False
stu.save()
```
#### 查询数据
```PYTHON
# 获得所有数据
print(Student.objects.all())
# 条件获取数据
print(Student.objects.get(id=1))
# 查询外键数据
print(Student.computer_set.all())
```
#### 修改数据
```PYTHON
stu = Student.objects.get(id=1)
stu.name = "我被改了"
stu.save()
```
#### 删除数据
```PYTHON
stu = Student.objects.get(id=1)
stu.delete()    # 删除
```

### 注册模型到后台管理界面
[main/admin.py](https://github.com/zhmhbest/HelloDjango/blob/master/main/admin.py)

## View
