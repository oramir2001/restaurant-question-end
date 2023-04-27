from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Category, Dish, Cart, Items, Delivery
from datetime import datetime as dt

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

@login_required(login_url='login')
def menu(request):
  category_list = Category.objects.all()
  return render(request, 'menu.html', {'category_list': category_list})

def logout(request):
  auth.logout(request)
  return redirect('login')

@login_required(login_url='login')
def show_dishes(request, id):
  category = Category.objects.get(id=id)
  dishes = Dish.objects.all()
  numbers = []
  for num in range(1,10):
    numbers.append(num)
  return render(request, 'show_dishes.html', {'category': category, "dishes":dishes, "numbers":numbers})

@login_required
def cart(request):
  cart = Cart.objects.filter(user_id=request.user.id).latest('id')
  cart_items = Items.objects.select_related('dish').filter(cart_id = cart.id)
  return render(request,'cart.html', {'cart_items': cart_items})

@login_required
def add_dish_to_cart(request):
    if request.method != 'POST':
      return None

    dish_id = request.POST.get('dish_id')
    amount = request.POST.get('amount')

    try:
      cart = Cart.objects.filter(user_id=request.user.id).latest('id')
    except Cart.DoesNotExist:
      cart = Cart.objects.create(user_id=request.user.id)

    item, created = Items.objects.get_or_create(
      cart_id=cart.id,
      dish_id=dish_id,
      defaults={'amount': amount}
    )

    if not created:
      item.amount += int(amount)
      item.save()
      item.refresh_from_db()

    return redirect('menu')

@login_required
def remove_dish_from_cart(request):
  if request.method == 'POST':
    cart_id = request.POST.get('cart_id')
    dish_id = request.POST.get('dish_id')
    Items.objects.filter(dish_id=dish_id, cart_id=cart_id).delete()
  return redirect('my-cart')

@login_required
def checkout(request):
  cart = Cart.objects.filter(user_id=request.user.id).latest('id')
  cart_items = Items.objects.select_related('dish').filter(cart_id = cart.id)
  sum = 0
  for item in cart_items:
    sum += (item.amount * item.dish.price)
  return render(request,'checkout.html', {'cart_items': cart_items, 'sum': sum})

@login_required
def submit_order(request):
  if request.method == 'POST':
    cart = Cart.objects.filter(user_id=request.user.id).latest('id')
    Delivery.objects.create(is_delivered=False, address=request.POST.get('address'), comment=request.POST.get('comment'), created=dt.now(), order_id=cart.id)
    Cart.objects.create(user_id=request.user.id)
    return redirect('thank-you')

@login_required
def thank_you(request):
  delivery= Delivery.objects.all().latest('order_id')
  delivery_items = Items.objects.filter(cart_id = delivery.order_id)
  sum = 0
  for item in delivery_items:
    sum += (item.amount * item.dish.price)
  return render(request,'thank_you.html', {'delivery': delivery, 'sum': sum })

@login_required
def orders(request):
  carts_and_items = {}
  carts = Cart.objects.filter(user_id=request.user.id)
  for cart in carts:
    cart_items = Items.objects.select_related('dish').filter(cart_id = cart.id)
    carts_and_items[cart] = cart_items
  return render(request, 'orders.html', {'carts_and_items': carts_and_items})

@login_required
def change_details(request):
  current_cart = Cart.objects.filter(user_id=request.user.id).latest('id')
  carts = Cart.objects.filter(user_id = request.user.id).exclude(id = current_cart.id)

  deliveries = []
  for cart in carts:
    delivery = Delivery.objects.get(order_id = cart.id)
    deliveries.append(delivery)

  return render(request, 'change_details.html', {'deliveries': deliveries})
