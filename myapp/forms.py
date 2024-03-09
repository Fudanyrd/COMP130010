# contain all forms needed by web pages.
from django import forms
from .models import Grade, Student, Course

class RegradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['grade']
        labels = {'text': ''}