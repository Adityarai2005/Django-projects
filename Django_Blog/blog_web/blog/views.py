from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .models import posts
from django.contrib.auth.models import User
from django.contrib.auth import decorators
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')
def sign(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        email = request.POST.get('email')
        password2=request.POST.get('password2')
        if password1==password2:
            user=User.objects.create_user(username=username,password=password1,email=email)
            user.save()
            return redirect('login')
        else:
            return redirect('signup')
    return render(request, 'signup.html')
      
# Create your views here.
@login_required(login_url='login')
def home(request):
   
    return render(request,'home.html',context={'posts':posts.objects.all()})
@login_required(login_url='login')
def my_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_username = request.POST.get('author')  # Get the username from the form

        try:
            author = User.objects.get(username=author_username)
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            return HttpResponse("User does not exist", status=400)

        # Create the post with the User instance as the author
        post = posts(title=title, content=content, author=author)
        post.save()
        return redirect('my_post')

    # Filter posts authored by the logged-in user
    print(request.user)
    for i in posts.objects.all():
        print(i.author)
    user_posts = posts.objects.filter(author=request.user)
    return render(request, 'my_post.html', context={'posts': user_posts})
def user_logout(request):
    logout(request)
    return redirect('login')
@login_required
def delete_post(request, pk):
  del_post=posts.objects.filter(id=pk)
  del_post.delete()
  return redirect('my_post')
 