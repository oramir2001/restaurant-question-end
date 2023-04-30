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

@login_required
def all_categories(request):
  if request.user.is_staff == True:
    categories = Category.objects.all()
    return render (request, 'all_categories.html', {'categories':categories})
  else:
    return redirect('menu')

@login_required
def all_dishes(request):
  if request.user.is_staff == True:
    dishes = Dish.objects.all()
    return render (request, 'all_dishes.html', {'dishes':dishes})
  else:
    return redirect('menu')

@login_required
def mark_as_delivered(request, order_id):
  if request.method == "POST":
    delivery = Delivery.objects.filter(order_id=order_id).latest('order_id')
    delivery.is_delivered = True
    delivery.save()
    return redirect('all-orders')
