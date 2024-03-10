# Code I wrote
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserSignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from .models import customUser as User
from Notifications.models import Notification
from courses.models import Course

# Create your views here.
# Registration View
def register(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page
    else:
        form = UserSignUpForm()
    return render(request, 'registration/register.html', {'form': form})

# Create or update view for profile
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def home(request):
    context = {
        'profile': request.user.profile,
    }
    if request.user.is_teacher:
        return render(request, 'users/teacher_home.html', context)
    else:
        return render(request, 'users/student_home.html', context)
    
# View to search for students
@login_required
def search_students(request):
    if not request.user.is_teacher:
        return redirect('home')
    query = request.GET.get('query', '')
    students = User.objects.filter(is_student=True, username__icontains=query) 
    return render(request, 'teachers_home.html', {'students': students})

# View for blocking and unblocking students
@login_required
def block_student(request, user_id):
    if request.user.is_teacher:  # Make sure only teachers can perform this action
        student = get_object_or_404(User, pk=user_id, is_student=True)
        student.is_blocked = True
        student.save()
    return redirect('home')  # Adjust the redirect as needed

@login_required
def unblock_student(request, user_id):
    if request.user.is_teacher:
        student = get_object_or_404(User, pk=user_id, is_student=True)
        student.is_blocked = False
        student.save()
    return redirect('home')

# For notification
def dashboard(request):
    message = f'{User.real_name or User.username} has enrolled in your course {Course.title}.'
    notifications = Notification.objects.filter(recipient=request.user, is_read=False)
    return render(request, 'dashboard.html', {'notifications': notifications})

# Search for user
def user_search(request):
    query = request.GET.get('query', '')
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.none()
    return render(request, 'users/user_search.html', {'users': users, 'query': query}) 

# Display user profile
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/user_profile.html', {'profile_user': user})

# End of Code I wrote