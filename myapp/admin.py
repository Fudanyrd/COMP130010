from django.contrib import admin

# Register your models here.
from myapp.models import Student, Course, Grade, Takes

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Takes)
