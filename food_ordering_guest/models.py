from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
# class FoodOrderingGuest(models.Model):
#   user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
#   phone = models.CharField(max_length=10)
#   address = models.CharField(max_length=20)
#   age = models.CharField(max_length=20)
#   id = models.CharField(max_length=9)

class Category(models.Model):
  name = models.CharField(max_length=30)
  image = models.CharField(max_length=500)

class Dish(models.Model):
  name = models.CharField(max_length=30)
  price = models.IntegerField(validators=[MaxValueValidator(999999999999999)])
  description = models.CharField(max_length=500)
  image = models.CharField(max_length=500)
  is_gluten_free = models.BooleanField(auto_created=False)
  is_vageterian = models.BooleanField(auto_created=False)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Items(models.Model):
  dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  amount = models.IntegerField(validators=[MaxValueValidator(999999999999999)])

class Delivery(models.Model):
  order = models.OneToOneField(Cart, on_delete=models.CASCADE)
  is_delivered = models.BooleanField(auto_created=False)
  address = models.CharField(max_length=500)
  comment = models.CharField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
