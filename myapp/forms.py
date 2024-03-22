# contain all forms needed by web pages.
from django import forms
from .models import Grade, Student, Course

class RegradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['grade']
        labels = {'text': ''}

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['grade']
        labels = {'text': ''}

class GradeAllForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student','grade']
        labels = {'text': 'student'}

class CourseFilter(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['cid', 'cname']
        labels = {'text': ''}
