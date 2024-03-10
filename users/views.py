from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))
