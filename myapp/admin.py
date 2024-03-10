from django.contrib import admin

# Register your models here.
from myapp.models import Student, Course, Grade, Takes, Instructor

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Takes)
admin.site.register(Instructor)
