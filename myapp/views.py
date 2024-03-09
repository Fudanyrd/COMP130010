from django.shortcuts import render
from .models import Student, Course, Grade 
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def courses(request):
    courses = Course.objects.order_by('cid')
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)
