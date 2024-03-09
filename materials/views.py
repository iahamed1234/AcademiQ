from django.shortcuts import render, redirect, get_object_or_404
# Code I wrote
from .forms import MaterialForm
from .models import Material
from courses.models import Course
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator

# Create your views here.
# View for Uploading Materials
@login_required
def add_material(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.course = course
            material.save()
            # Redirect to a new URL:
            return redirect('materials:material_list', course_id=course.id)
    else:
        form = MaterialForm()
    return render(request, 'materials/add_material.html', {'form': form, 'course': course})

# View to list material
class MaterialListView(ListView):
    model = Material
    template_name = 'materials/material_list.html'  # Ensure this template exists
    context_object_name = 'materials'

    def get_queryset(self):
        """
        This method is overridden to filter materials for a specific course.
        """
        course_id = self.kwargs.get('course_id')
        course = get_object_or_404(Course, id=course_id)  # Ensure Course model is imported
        return Material.objects.filter(course=course)
# End of Code I wrote