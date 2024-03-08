# Code I Wrote
from django import forms
from .models import Course

#form to create a course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'teacher']

# End of Code I Wrote