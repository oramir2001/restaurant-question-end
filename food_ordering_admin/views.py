from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from food_ordering_guest.models import Category, Dish, Cart, Items, Delivery
from datetime import datetime as dt

@login_required
def staff_menu(request):
  if request.user.is_staff == True:
    return render (request, 'staff_menu.html')
  else:
    return redirect('menu')

@login_required
def all_orders(request):
  if request.user.is_staff == True:
    deliveries = Delivery.objects.all()
    return render (request, 'all_orders.html',  {'deliveries': deliveries})
  else:
    return redirect('menu')

# @login_required
# def change_details(request):
#   if request.user.is_staff == True:
#     return render (request, 'change_details.html')
#   else:
#     return redirect('menu')

@login_required
def all_categories(request):
  if request.user.is_staff == True:
    return render (request, 'all_categories.html')
  else:
    return redirect('menu')

@login_required
def all_dishes(request):
  if request.user.is_staff == True:
    return render (request, 'all_dishes.html')
  else:
    return redirect('menu')
