from django.shortcuts import render, redirect
from .models import Brajbhumi
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('form', form)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'brij/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        print('username', username)
        password = request.POST['password']
        print('password', password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'brij/login.html', {'error': 'Invalid credentials'})
    return render(request, 'brij/index.html')




def index(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        text = request.POST.get('subject')
        city = request.POST.get('city')

        if firstname and lastname and phone and text and city:
            data = Brajbhumi(name=firstname, lastname=lastname, phone=phone, choice=city, textfield=text)
            data.save()
            return redirect('success')
    return render(request, 'brij/index.html')


def form(request):
    return render(request,'brij/form.html')

def success(request):
    return render(request,'brij/success.html')