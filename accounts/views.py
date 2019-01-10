from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already exists.')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email has already being used.')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                messages.success(request, 'User created. You may now log in.')
                return redirect('login')
        else:
            messages.error(request, "Paswords do not match.")
            return redirect('register')
    return render(request, 'accounts/register.html')


@login_required
def logout(request):
    # if request.method == "POST":
    #     auth.logout(request)
    #     messages.success(request, "You are now logged out.")
    #     return redirect('login')
    auth.logout(request)
    messages.success(request, "You are now logged out.")
    return redirect('login')


@login_required()
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
