from django.contrib import admin

# Register your models here.
from main.models import Student
from main.models import Computer

admin.site.register(Student)
admin.site.register(Computer)
