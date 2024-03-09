# Code I wrote
from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]

# End of Code I wrote