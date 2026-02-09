from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re

#Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            return render(request, 'accounts/login.html', {
                'error': 'Both fields are required.'
            })
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password.'
            })
            
    return render(request, 'accounts/login.html')

#Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

#Register View
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            return render(request, 'accounts/register.html', {
                'error': 'All fields are required.'
            })

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            return render(request, 'accounts/register.html', {
                'error': 'Invalid email format.'
            })

        if len(password) < 8:
            return render(request, 'accounts/register.html', {
                'error': 'Password must be at least 8 characters long.'
            })

        if not re.search(r'[A-Z]', password):
            return render(request, 'accounts/register.html', {
                'error': 'Password must contain at least one uppercase letter.'
            })

        if not re.search(r'[a-z]', password):
            return render(request, 'accounts/register.html', {
                'error': 'Password must contain at least one lowercase letter.'
            })

        if not re.search(r'[0-9]', password):
            return render(request, 'accounts/register.html', {
                'error': 'Password must contain at least one digit.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {
                'error': 'Username already exists.'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {
                'error': 'Email already exists.'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'accounts/register.html')
