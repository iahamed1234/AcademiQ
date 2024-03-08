from django.shortcuts import render
# Code I wrote
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import Course

# Create your views here.
@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user  # Set the teacher to the current user
            course.save()
            return redirect('courses:list_courses')  # Redirect to the course listing page
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

@login_required
def list_courses(request):
    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'courses/list_courses.html', {'courses': courses})

# End of Code I wrote