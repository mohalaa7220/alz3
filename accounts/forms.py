from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


# ==================== Register Forms ====================
class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)
    age = forms.IntegerField(required=False)
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')])
    education_level = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'email', 'phone_number',
                  'age', 'gender', 'education_level', 'password1', 'password2']


# ==================== Login Forms ====================
class CustomUserLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
