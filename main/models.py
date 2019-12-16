from django.db import models


# 模型设计代码
class Student(models.Model):
    # id: 自动添加，不需要手动设计
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    birthday = models.DateField()
    is_del = models.BooleanField()


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
