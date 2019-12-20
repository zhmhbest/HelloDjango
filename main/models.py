# coding=utf-8
from django.db import models


# 模型设计代码
class Student(models.Model):
    # id: 自动添加，不需要手动设计
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    birthday = models.DateField()
    is_del = models.BooleanField()
    """
        自增: models.AutoField()
        字符串: models.CharField(max_length=?)
        大文本: models.TextField()
        整形: models.IntegerField()
        完全浮点数: models.DecimalField(max_digits=None, decimal_places=None)
        计算浮点数: models.FloatField()
        日期: models.DateField(auto_now=False, auto_now_add=False)
        时间: models.TimeField(auto_now=False, auto_now_add=False)
        日期+时间: models.DateTimeField(auto_now=False, auto_now_add=False)
        文件: models.FileField()
        图片: models.ImageField()
    """
    """
        primary_key:    主键
        unique:         不可重复
        db_index:       加索引
        db_column:      自定义列名
        null:           允许为null
        blank:          后台管理添加时，是否可以不填写
    """


class Computer(models.Model):

    """
    定义外键
        CASCADE:    删除关联数据，与之关联的数据也删除
        DO_NOTHING: 删除关联数据，什么也不做
        SET_NULL:   删除关联数据，与之关联的值设置为null
        PROTECT:    删除关联数据，引发错误ProtectedError
        SET:        删除关联数据，与之关联的值设置为指定的值
    """
    holder = models.ForeignKey('Student', on_delete=models.SET_NULL, blank=True, null=True)
