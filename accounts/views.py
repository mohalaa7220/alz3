from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserRegistrationForm, CustomUserLoginForm


# ==================== Register View ====================

def register_view(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
    else:
        form = CustomUserRegistrationForm()
    return render(request, "auth/register.html", {"form": form})


# ==================== Login View ====================

def login_view(request):
    if request.method == "POST":
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")  # Redirect to home page
    else:
        form = CustomUserLoginForm()
    return render(request, "auth/login.html", {"form": form})


# ==================== Logout View ====================

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")
