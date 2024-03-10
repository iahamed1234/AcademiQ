# Code I wrote
from django.urls import path
from . import views
from .views import view_feedback

app_name = 'feedback'

urlpatterns = [
    path('course/<int:course_id>/feedback/submit/', views.submit_feedback, name='submit_feedback'),
    path('course/<int:course_id>/feedback/', views.feedback_list, name='feedback_list'),
    path('course/<int:course_id>/feedback/', view_feedback, name='view_feedback'),
    
]
# End of Code I wrote