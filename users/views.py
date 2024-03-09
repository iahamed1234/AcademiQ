from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib.auth import login

# Create your views here.
# Registration View
def register(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page or any other page
    else:
        form = UserSignUpForm()
    return render(request, 'registration/register.html', {'form': form})
