# Django

## MVT
- M: 模型，对应MVC的M，用于与数据库交互。
- V: 视图，对应MVC的C，用于接受请求和响应数据。
- T: 模板，对应MVC的V，用于决定最终显示样式。


## Shell命令
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
    │  │  models.py                     设计和数据库中表对应的类
    │  │  views.py                      接受请求、返回应答
    │  │  tests.py                      写测试代码的文件
    │  │  __init__.py
    │  │
    │  └─migrations
    │          __init__.py
    │
    └─templates

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

### 可视化管理
#### 语言本地化
[HelloDjango/settings.py#105](https://github.com/zhmhbest/HelloDjango/blob/master/HelloDjango/settings.py#L105)
```PYTHON
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```