from django.shortcuts import render, get_object_or_404
# Code I wrote
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import Course
from Notifications.models import Notification
from django.views.generic import ListView
from users.models import customUser as User

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

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'course_list'

def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/list_courses.html', {'courses': courses})

# View to remove students from course
# @login_required
# def remove_student(request, course_id, user_id):
#     if request.user.is_teacher:
#         course = get_object_or_404(Course, pk=course_id)
#         student = get_object_or_404(User, pk=user_id, is_student=True)
#         # Assuming there's a ManyToManyField relationship named "students" on your Course model
#         course.students.remove(student)
#         course.save()
#         # Redirect back to the course detail page or wherever appropriate
#         return redirect('course_detail', course_id=course_id)
#     else:
#         # Redirect to home
#         return redirect('home')
    
# View for enrollment
@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        # Add the current user to the enrolled_students
        course.enrolled_students.add(request.user)
        # Create a notification for the teacher
        Notification.objects.create(
            recipient=course.teacher,
            message=f"{User.username} has enrolled in your course: {course.title}."
        )
        return redirect('courses:list_courses')  # Redirect to a confirmation page or back to the course list
    else:
        # Show a confirmation page or form before enrolling
        return render(request, 'courses/enroll_confirm.html', {'course': course})

# End of Code I wrote