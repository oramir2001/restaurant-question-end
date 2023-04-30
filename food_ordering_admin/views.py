from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from food_ordering_guest.models import Category, Dish, Cart, Items, Delivery
from datetime import datetime as dt
from django.core.exceptions import ValidationError
from django.conf import settings
import os

@login_required
def staff_menu(request):
  if not request.user.is_staff:
    return redirect('menu')

  return render (request, 'staff_menu.html')

@login_required
def all_orders(request):
  if not request.user.is_staff:
    return redirect('menu')

  deliveries = Delivery.objects.all()
  return render (request, 'all_orders.html',  {'deliveries': deliveries})

@login_required
def all_categories(request):
  if not request.user.is_staff:
    return redirect('menu')

  categories = Category.objects.all()
  return render (request, 'all_categories.html', {'categories':categories})

@login_required
def create_category(request):
  if not request.user.is_staff:
    return redirect('menu')

  if request.method == 'POST':
    image_file = request.FILES.get('image')

    if image_file:
      with open(os.path.join(settings.MEDIA_ROOT, image_file.name), 'wb+') as destination:
        for chunk in image_file.chunks():
          destination.write(chunk)

    new_category = Category(
      name = request.POST.get('name'),
      image = image_file.name if image_file else None
    )

    try:
      new_category.full_clean()
      new_category.save()
    except ValidationError as e:
      for field, errors in e.message_dict.items():
        for error in errors:
          print(f"{field}: {error}")

    return redirect('all-categories')

@login_required
def new_category(request):
  if not request.user.is_staff:
    return redirect('menu')

  return render (request, 'new_category.html')

@login_required
def all_dishes(request):
  if not request.user.is_staff:
    return redirect('menu')

  dishes = Dish.objects.all()
  return render (request, 'all_dishes.html', {'dishes':dishes})

@login_required
def mark_as_delivered(request, order_id):
  if not request.user.is_staff:
    return redirect('menu')

  if request.method == "POST":
    delivery = Delivery.objects.filter(order_id=order_id).latest('order_id')
    delivery.is_delivered = True
    delivery.save()
    return redirect('all-orders')
