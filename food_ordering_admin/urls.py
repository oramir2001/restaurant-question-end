from django.urls import path
from . import views

urlpatterns=[
  path('staff-menu/', views.staff_menu, name='staff-menu'),
  path('staff-menu/all-orders/', views.all_orders, name='all-orders'),
  path('staff-menu/all-categories/', views.all_categories, name='all-categories'),
  path('staff-menu/all-dishes/', views.all_dishes, name='all-dishes'),
  path('orders/<int:order_id>/mark-as-delivered', views.mark_as_delivered, name='mark-as-delivered'),
  path('create-category/', views.create_category, name='create-category'),
  path('new-category/', views.new_category, name='new-category')
]

