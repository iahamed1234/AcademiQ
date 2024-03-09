# Code I wrote
from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('course/<int:course_id>/feedback/submit/', views.submit_feedback, name='submit_feedback'),
    path('course/<int:course_id>/feedback/', views.feedback_list, name='feedback_list'),
]

# End of Code I wrote