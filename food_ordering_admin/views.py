from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.


def staff_homepage(request):
  return render (request, 'staff_homepage.html')

def staff_login(request):
  # if request.method == "POST":
  #   user = auth.authenticate(
  #     request,
  #     username=request.POST['username'],
  #     password=request.POST['password']
  # )
  return render (request, 'staff_login.html')

# @login_required(login_url='login')
def staff_menu(request):
  return render (request, 'staff_menu.html')

# def logout(request):
#   auth.logout(request)
#   return redirect('staff-login')

def all_orders(request):
  return render (request, 'all_orders.html')

def all_categories(request):
  return render (request, 'all_categories.html')

def all_dishes(request):
  return render (request, 'all_dishes.html')











# def signup_staff(request):
#   if request.method == "POST":
#     new_user = User(
#       first_name = request.POST['first_name'],
#       last_name = request.POST['last_name'],
#       username = request.POST['username'],
#       email = request.POST['email'],
#       password = make_password(request.POST['password']),
#       is_staff = request.POST.get('is_staff') == 'on'
#     )
#     new_user.save()
#     return redirect('login')
#   return render(request,'signup_staff.html')









# def login(request):
#   if request.method == "POST":
#     user = auth.authenticate(
#       request,
#       username=request.POST['username'],
#       password=request.POST['password']
#     )
#     if user is not None:
#       auth.login(request,user)
#       return redirect('menu')
#   return render(request,'login.html')
