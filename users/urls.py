# Code I wrote
from django.urls import path
from .views import register
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('search_students/', views.search_students, name='search_students'),
    path('block_student/<int:user_id>/', views.block_student, name='block_student'),
    path('unblock_student/<int:user_id>/', views.unblock_student, name='unblock_student'),
    path('search/', views.user_search, name='user_search'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),

]
# End of Code I wrote