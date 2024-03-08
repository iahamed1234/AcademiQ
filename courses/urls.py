# Code I wrote
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('create/', views.create_course, name='create_course'),
    path('', views.list_courses, name='list_courses'),
]

# End of Code I wrote