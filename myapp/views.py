from django.shortcuts import render
from .models import Student, Course, Grade 
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import RegradeForm

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

    context = {
        'course': course,
        'grades': grades
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