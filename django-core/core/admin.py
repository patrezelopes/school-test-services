from django.contrib import admin
# Register your models here.

from core.models import Student, School, Exam

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Exam)
