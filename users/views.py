from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
import mysql.connector

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))

class Admin():
    def __init__(self, username, email):
        self.username = username
        self.email = email

def help(request):
    # this is not login required. Anyone can access this page.
    connection = mysql.connector.connect(
        user = 'root',
        password = 'Yrd37538311',
        database='grade',    
        host = 'db',
        port = '3306',
    )
    cursor = connection.cursor()
    cursor.execute(
        """
        select email, username from auth_user where is_superuser = 1 order by username
        """
    )
    admins = []
    for tp in cursor.fetchall():
        admins.append(Admin(tp[1], tp[0]))
    
    cursor.close()
    connection.close()

    context = {
        'admins': admins
    }
    return render(request, 'help.html', context)
