from django.shortcuts import render
from .models import Student, Course, Grade, Takes, Instructor
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models.expressions import RawSQL
from django.contrib.auth.decorators import login_required
from .forms import RegradeForm, GradeForm, GradeAllForm
import mysql.connector

def avg_grade(course_id):
    """ given the course id, calculate its average grade"""
    connection = mysql.connector.connect(
        user = 'root',
        password = 'Yrd37538311',
        database = 'grade'
    )
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT AVG(grade) from myapp_grade where course_id = {course_id}
        """
    )
    res = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return res

# citation: <https://docs.djangoproject.com/en/5.0/ref/models/querysets/>
"""
User can have 3 types: student, instructor, admin(from academic affair center).
Thus we need some method to tell them apart. My machanism is that:
1. look in the `myapp_auth` table, if it is a superuser(admin), over.
2. look in the `myapp_instructor` table, if found, return 'instructor'
3. the user is student.
"""
def usertype(request):
    """ return the type of the user. None|instructor|student|admin"""
    if not request.user.is_authenticated:
        return None
    if len(Instructor.objects.filter(tid=request.user.username)) != 0:
        return 'instructor'
    if len(Student.objects.filter(sid=request.user.username)) != 0:
        return 'student'
    return 'admin'  # those who can login but is not student/instructor is admin

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def courses(request):
    """ admin has access to all courses; while instructor only have access to the courses he/she taught"""
    ut = usertype(request)
    if ut == 'admin':
        courses = Course.objects.order_by('cid')
    elif ut == 'instructor':
        instructor = (Instructor.objects.filter(tid=request.user.username))[0]
        courses = Course.objects.filter(teacher=instructor).order_by('cid')
    else:
        raise Http404
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)

@login_required
def grades(request, course_id):
    ut = usertype(request)
    if ut == 'student':
        # student doen't have access to this page!
        raise Http404

    course = Course.objects.get(id = course_id)
    if ut != 'admin':
        if course.teacher.tid != request.user.username:
            # the instructor wants to access grades of course he doesn't teach...
            raise Http404
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

@login_required
def gradetb(request, course_id):
    ut = usertype(request)
    if ut == 'student':
        # student doen't have access to this page!
        raise Http404

    course = Course.objects.get(id = course_id)
    if ut != 'admin':
        if course.teacher.tid != request.user.username:
            # the instructor wants to access grades of course he doesn't teach...
            raise Http404
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
        'average': str(avg_grade(course_id)),
        'ungraded': Student.objects.filter(id__in=ungraded).order_by("sname"),
    }
    return render(request, 'gradetb.html', context)

@login_required
def regrade(request, grade_id):
    """ regrade a entry(on course, student)"""
    ut = usertype(request)
    if ut == 'student':
        # student doen't have access to this page!
        raise Http404

    grade_obj = Grade.objects.get(id=grade_id)
    course = grade_obj.course
    if ut == 'instructor':
        if course.teacher.tid != request.user.username:
            raise Http404
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

@login_required
def givegrade(request, course_id, student_id):
    """ give a student his/her grade"""
    ut = usertype(request)
    if ut == 'student':
        # student doen't have access to this page!
        raise Http404

    student = Student.objects.get(id=student_id)
    course = Course.objects.get(id=course_id)
    if ut == 'instructor':
        if course.teacher.tid != request.user.username:
            raise Http404

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

@login_required
def gradeall(request, course_id):
    ut = usertype(request)
    if ut == 'student':
        # student doen't have access to this page!
        raise Http404

    course = Course.objects.get(id=course_id)
    if ut == 'instructor':
        if course.teacher.tid != request.user.username:
            raise Http404
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