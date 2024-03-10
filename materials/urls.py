# Code I wrote
from django.urls import path
from .views import add_material, MaterialListView

app_name = 'materials'

urlpatterns = [
    path('course/<int:course_id>/add/', add_material, name='add_material'),
    path('course/<int:course_id>/materials/', MaterialListView.as_view(), name='material_list'),
]

# End of Code I wrote