from django.shortcuts import render

# Home View
def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            # Logic for teachers
            return render(request, 'teachers_home.html')
        elif request.user.is_student:
            # Logic for students
            return render(request, 'students_home.html')
    return render(request, 'home.html')

