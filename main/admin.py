from django.contrib import admin

# Register your models here.
from main.models import Student
admin.site.register(Student)

from main.models import Computer
admin.site.register(Computer)