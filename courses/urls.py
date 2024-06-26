# Code I wrote
from django.urls import path
from . import views
# from .views import remove_student

app_name = 'courses'

urlpatterns = [
    path('create/', views.create_course, name='create_course'),
    path('', views.list_courses, name='list_courses'),
    path('<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
]

# End of Code I wrote