from django.shortcuts import render
from django.http import HttpResponse
from todo_app import models
from .models import TODOO
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.db import IntegrityError
def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        # Check if passwords match
        if password1 != password2:
            return render(request, 'sign.html', {'error': 'Passwords do not match'})

        # Check if username already exists
        try:
            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('login')  # Redirect to login page after successful signup
        except IntegrityError:
            return render(request, 'sign.html', {'error': 'Username already exists'})

    return render(request, 'sign.html')
def login(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(req,username=username,password=password)
        if user is not None:
            return redirect('todo')
        else:
            return render(req,'login.html')
    return render(req,'login.html')
def todo_view(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        models.TODOO.objects.create(title=title, user=request.user)
        
        return redirect('todo')

    todos = TODOO.objects.filter(user=request.user)
    return render(request, 'todo.html', {'todos': todos})

def delete_todo(request,srno):
    TODOO.objects.filter( user=request.user,srno=srno).delete()
    return redirect('todo')