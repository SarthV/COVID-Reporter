from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'username taken')
            return redirect('login')
    
    else:
        return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():   
            messages.info(request, 'Email id taken')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email = email, password = password, first_name = first_name, last_name = last_name)
            user.save();
            return redirect('login')
        
        return redirect('/')
    else:
        return render(request, 'signup.html') 