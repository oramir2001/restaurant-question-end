from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from food_ordering_guest.models import Category, Dish, Delivery
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

    new_category.save()
    return redirect('all-categories')

@login_required
def new_category(request):
  if not request.user.is_staff:
    return redirect('menu')

  return render (request, 'new_category.html')

@login_required
def edit_category(request, category_id):
  if not request.user.is_staff:
    return redirect('menu')

  category = Category.objects.filter(id=category_id).latest('id')

  return render(request, 'edit_category.html', {'category': category})


@login_required
def update_category(request, category_id):
  if not request.user.is_staff:
    return redirect('menu')

  if request.method == "POST":
    category = Category.objects.filter(id=category_id).latest('id')
    category.name = request.POST.get('name')
    image_file = request.FILES.get('image')

    if image_file:

      with open(os.path.join(settings.MEDIA_ROOT, image_file.name), 'wb+') as destination:
        for chunk in image_file.chunks():
          destination.write(chunk)

      category.image = image_file.name

    category.save()
    return redirect('all-categories')

@login_required
def delete_category(request, category_id):
  if not request.user.is_staff:
    return redirect('menu')

  if request.method == "POST":
    Category.objects.filter(id=category_id).delete()

  return redirect('all-categories')

@login_required
def all_dishes(request):
  if not request.user.is_staff:
    return redirect('menu')

  dishes = Dish.objects.all()
  return render (request, 'all_dishes.html', {'dishes': dishes})

@login_required
def create_dish(request):
  if not request.user.is_staff:
    return redirect('menu')

  if request.method == 'POST':
    image_file = request.FILES.get('image')

    if image_file:
      with open(os.path.join(settings.MEDIA_ROOT, image_file.name), 'wb+') as destination:
        for chunk in image_file.chunks():
          destination.write(chunk)

    new_dish = Dish(
      name = request.POST.get('name'),
      price = int(request.POST.get('price')),
      description = request.POST.get('description'),
      image = image_file.name if image_file else None,
      is_gluten_free = bool(request.POST.get('is_gluten_free')),
      is_vageterian = bool(request.POST.get('is_vageterian')),
      category_id = int(request.POST.get('category_id'))
    )

    new_dish.save()
    return redirect('all-dishes')

@login_required
def new_dish(request):
  if not request.user.is_staff:
    return redirect('menu')

  categories = Category.objects.all()
  return render (request, 'new_dish.html', {'categories': categories})

@login_required
def edit_dish(request, dish_id):
  if not request.user.is_staff:
    return redirect('menu')

  dish = Dish.objects.filter(id=dish_id).latest('id')
  categories = Category.objects.all()

  return render(request, 'edit_dish.html', {'dish': dish, 'categories':categories})


@login_required
def update_dish(request, dish_id):
  if not request.user.is_staff:
    return redirect('menu')

  if request.method == "POST":
    dish = Dish.objects.filter(id=dish_id).latest('id')
    dish.name = request.POST.get('name')
    dish.price = int(request.POST.get('price'))
    dish.description = request.POST.get('description')
    dish.is_gluten_free = bool(request.POST.get('is_gluten_free'))
    dish.is_vageterian = bool(request.POST.get('is_vageterian'))
    dish.category_id = int(request.POST.get('category_id'))
    image_file = request.FILES.get('image')

    if image_file:
      with open(os.path.join(settings.MEDIA_ROOT, image_file.name), 'wb+') as destination:
        for chunk in image_file.chunks():
          destination.write(chunk)

      dish.image = image_file.name

    dish.save()
    return redirect('all-dishes')

@login_required
def delete_dish(request, dish_id):
  if not request.user.is_staff:
    return redirect('menu')

  if request.method == "POST":
    Dish.objects.filter(id=dish_id).delete()

  return redirect('all-dishes')

@login_required
def mark_as_delivered(request, order_id):
  if not request.user.is_staff:
    return redirect('menu')

  if request.method == "POST":
    delivery = Delivery.objects.filter(order_id=order_id).latest('order_id')
    delivery.is_delivered = True
    delivery.save()
    return redirect('all-orders')
