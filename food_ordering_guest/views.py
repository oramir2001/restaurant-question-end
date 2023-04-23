from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Category, Dish, Cart, Items

from pprint import pprint
import inspect

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
      return redirect('menu')
  return render(request,'login.html')

def logout(request):
  auth.logout(request)
  return redirect('login')

@login_required(login_url='login')
def menu(request):
  category_list = Category.objects.all()
  return render(request, 'menu.html', {'category_list': category_list})

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

@login_required
def starters(request):
  dish_list = Dish.objects.filter(category_id=1).values()
  return render(request,'starters.html', {'dish_list': dish_list})

@login_required
def mains(request):
  dish_list = Dish.objects.filter(category_id=2).values()
  return render(request,'mains.html', {'dish_list': dish_list})

@login_required
def desserts(request):
  dish_list = Dish.objects.filter(category_id=3).values()
  return render(request,'desserts.html', {'dish_list': dish_list})

@login_required
def drinks(request):
  dish_list = Dish.objects.filter(category_id=4).values()
  return render(request,'drinks.html', {'dish_list': dish_list})

@login_required
def cart(request):
  cart = Cart.objects.get(user_id=request.user.id)
  cart_items = Items.objects.select_related('dish').filter(cart_id = cart.id)
  return render(request,'cart.html', {'cart_items': cart_items})

@login_required
def add_dish_to_cart(request):
  if request.method == 'POST':
    cart = Cart.objects.get(user_id=request.user.id)
    dish_id = request.POST.get('dish_id')
    dish_item = Items(cart_id=cart.id, dish_id = dish_id, amount=1)
    dish_item.save()
    return redirect('my-cart')

# @login_required
# def remove_dish(request):
#   return render(request,'remove_dish.html')

# @login_required
# def checkout(request):
#   return render(request,'checkout.html')
