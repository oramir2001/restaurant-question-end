from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import FoodOrderingGuest
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import auth

def homepage(request):
  return render(request,'homepage.html')

def login_user(request):
  if request.method == "POST":
    user = auth.authenticate(
      request,
      username=request.POST['username'],
      password=request.POST['password']
    )
    if user is not None:
      auth.login(request,user)
      return redirect('show_account')
  return render(request,'login.html')

def logout(request):
  auth.logout(request)
  return redirect('login')

@login_required(login_url='login')
def show_account(request):
  return render(request,'account.html')

def signup(request):
  if request.method == "POST":
    new_user = User(
      first_name = request.POST['first_name'],
      last_name = request.POST['last_name'],
      username = request.POST['username'],
      email = request.POST['email'],
      password = make_password(request.POST['password'])
    )
    new_user.save()
    return redirect('login')
  return render(request,'signup.html')

def starters(request):
  return render(request,'starters.html')

def mains(request):
  return render(request,'mains.html')

def desserts(request):
  return render(request,'desserts.html')

def drinks(request):
  return render(request,'drinks.html')
