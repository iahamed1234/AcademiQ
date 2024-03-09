from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

User = get_user_model()

class UserSignUpForm(UserCreationForm):
    real_name = forms.CharField(required=False)
    photo = forms.ImageField(required=False)
    # Add choices for user role
    user_role = forms.ChoiceField(choices=[('teacher', 'Teacher'), ('student', 'Student')])

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('real_name', 'photo',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.real_name = self.cleaned_data.get('real_name')
        user_role = self.cleaned_data['user_role']
        if user_role == 'teacher':
            user.is_teacher = True
            user.is_student = False
        else:
            user.is_student = True
            user.is_teacher = False

        if commit:
            user.save()
            if self.cleaned_data['photo']:
                user.photo = self.cleaned_data['photo']
                user.save()
        return user

# To update profile on respective home page
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'status_update', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

