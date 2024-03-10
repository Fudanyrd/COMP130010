from django.db import models
# reference: <https://docs.djangoproject.com/en/5.0/ref/models/fields/#decimalfield>

# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=20)
    sname = models.CharField(max_length=50)
    gender = models.CharField(max_length=4)
    year = models.IntegerField()
    faculty = models.CharField(max_length=50)

    def __str__(self):
        return self.sid + '-' +self.sname

class Instructor(models.Model):
    tid = models.CharField(max_length=20)
    tname= models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)

class Course(models.Model):
    cid = models.CharField(max_length=20) 
    cname = models.CharField(max_length=50)
    credit = models.IntegerField()
    teacher = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.cid + '-' + self.cname

class Takes(models.Model):
    """ represent students takes courses"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.sname + '-' + self.course.cname

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # grades of students won't exceed 100.00, decimal place won't exceed two.
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def bar_chart(self) -> str:
        """ return the bar chart representation"""
        value = int(self.grade)
        repr = ''
        for i in range(value // 2):
            repr += '='
        repr += '>'
        for i in range(50 - value // 2):
            repr += ' '
        repr += '|'
        repr += str(self.grade)
        return repr
    
    def passed(self) -> bool:
        """ return true if student passed the course."""
        return float(self.grade) >= 60.0

    def __str__(self):
        return str(self.student) + ': ' + str(self.grade)
