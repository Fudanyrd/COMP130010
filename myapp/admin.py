from django.contrib import admin

# Register your models here.
from myapp.models import Student, Course, Grade

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Grade)
