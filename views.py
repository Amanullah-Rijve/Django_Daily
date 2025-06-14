from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, LoginForm

# Temporary session storage
user_storage = {}

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user_storage[email] = password  # Simulate user storage

            messages.success(request, 'Signup successful! Please login.')
            return redirect('login')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if email in user_storage and user_storage[email] == password:
                messages.success(request, 'Login successful!')
                return redirect('login')  # You can redirect to home/dashboard
            else:
                messages.error(request, 'Invalid email or password.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
