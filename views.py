from django.shortcuts import render, redirect
from .models import Company, Placement, Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    companies = Company.objects.all()
    return render(request, 'placement_app/home.html', {'companies': companies})

def register_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        roll_no = request.POST['roll_no']
        dept = request.POST['department']
        cgpa = request.POST['cgpa']

        user = User.objects.create_user(username=username, password=password)
        Student.objects.create(user=user, roll_no=roll_no, department=dept, cgpa=cgpa)
        return redirect('login')
    return render(request, 'placement_app/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'placement_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'placement_app/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


# Create your views here.
