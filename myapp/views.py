from django.shortcuts import render
from .models import Student, Course, Grade, Takes
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models.expressions import RawSQL
from django.contrib.auth.decorators import login_required
from .forms import RegradeForm, GradeForm, GradeAllForm
import mysql.connector

# citation: <https://docs.djangoproject.com/en/5.0/ref/models/querysets/>

# Create your views here.
def index(request):
    return render(request, 'index.html')

def courses(request):
    courses = Course.objects.order_by('cid')
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)

def grades(request, course_id):
    course = Course.objects.get(id = course_id)
    # order the grades in descending order
    grades = course.grade_set.order_by('-grade')
    ungraded=RawSQL(
        f"""
        select student_id from myapp_takes where(
          course_id={course_id} and student_id not in(
            select student_id from myapp_grade where myapp_grade.course_id={course_id}
          )
        )
        """, []
    )

    context = {
        'course': course,
        'grades': grades,
        'ungraded': Student.objects.filter(id__in=ungraded).order_by("sname"),
    }
    return render(request, 'grades.html', context)

def regrade(request, grade_id):
    """ regrade a entry(on course, student)"""
    grade_obj = Grade.objects.get(id=grade_id)
    course = grade_obj.course
    if request.method != 'POST':
        form = RegradeForm(instance=grade_obj)
    else:
        form = RegradeForm(instance=grade_obj,data=request.POST)
        if form.is_valid():
            form.save()
            # get the course id and redirect there.
            return HttpResponseRedirect(reverse('myapp:grades', args=[course.id]))
    context = {'form': form, 'grade': grade_obj, 'course': course}
    return render(request, 'regrade.html', context)

def givegrade(request, course_id, student_id):
    """ give a student his/her grade"""
    student = Student.objects.get(id=student_id)
    course = Course.objects.get(id=course_id)

    if request.method != "POST":
        form = GradeForm()
    else:
        form = GradeForm(data=request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.student = student
            grade.course = course
            grade.save()
            return HttpResponseRedirect(reverse('myapp:grades', args=[course.id]))
    context = {
        'course': course,
        'student': student,
        'form': form,
    }
    return render(request, 'givegrade.html', context)

def GradeAllHelper(
    form: GradeForm,
    student,
    course,
) -> bool:
    """ help gradeall commit changes, return true if the form is valid"""
    if form.is_valid():
        grade = form.save(commit=False)
        grade.save()
        return True
    return False

def gradeall(request, course_id):
    course = Course.objects.get(id=course_id)
    ungraded = set()
    raw=RawSQL(
        f"""
        select student_id from myapp_takes where(
          course_id={course_id} and student_id not in(
            select student_id from myapp_grade where myapp_grade.course_id={course_id}
          )
        )
        """, []
    )
    for student in Student.objects.filter(id__in=raw):
        ungraded.add(student.id) 
    each = RawSQL(  # find id of student who has taken the course, all of them
        f"""
        select student_id from myapp_takes where course_id = {course_id}
        """, []
    )
    students = Student.objects.filter(id__in=each).order_by('sname')
    if request.method == 'POST':
        print(request.POST['grade'])
        print(request.POST.getlist('grade'))
        for i in range(len(students)):
            if students[i].id not in ungraded:
                grade = (Grade.objects.filter(student=students[i]).filter(course=course))[0]
                grade.grade = request.POST.getlist('grade')[i]
                grade.save()
                continue
            grade = Grade()
            grade.course = course
            grade.student = students[i]
            grade.grade = request.POST.getlist('grade')[i]
            grade.save()
        return HttpResponseRedirect(reverse('myapp:grades', args=[course.id]))

    forms = []
    for student in students:
        if student.id in ungraded:
            grade = Grade()
            grade.course = course
            grade.student = student
            forms.append(GradeAllForm(instance = grade))
        else:
            grade = (Grade.objects.filter(student=student).filter(course=course))[0]
            forms.append(GradeAllForm(instance = grade))
    context = {
        'course': course,
        'forms': forms,
        'students': students,
    } 
    return render(request, 'gradeall.html', context)