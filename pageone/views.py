from django.shortcuts import render, redirect
from .models import news, contact
from django.http import HttpResponse
from .forms import contactform
from django.contrib import messages

# Create your views here.
def home(request):
    News = news.objects.all()
    return render(request, 'home.html', {'News' : News})

def listings(request):
    cont = contact.objects.all()
    return render(request, 'listings.html', {'listings' : cont})

def fillinfo(request):
    form = contactform(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user;
            obj.save()
            return redirect('/')
    return render(request, 'forms.html', {'form' : form})    