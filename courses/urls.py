# Code I wrote
from django.urls import path
from . import views
# from .views import remove_student

app_name = 'courses'

urlpatterns = [
    path('create/', views.create_course, name='create_course'),
    path('', views.list_courses, name='list_courses'),
    # path('course/<int:course_id>/remove_student/<int:user_id>/', remove_student, name='remove_student'),
    path('<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
]

# End of Code I wrote