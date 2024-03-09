from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback
from courses.models import Course
# Code I wrote

# Create your views here.
@login_required
def submit_feedback(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.course = course
            feedback.save()
            return redirect('feedback:feedback_list', course_id=course.id)
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit_feedback.html', {'form': form, 'course': course})

@login_required
def feedback_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    feedbacks = Feedback.objects.filter(course=course)
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks, 'course': course})
# End of Code I wrote