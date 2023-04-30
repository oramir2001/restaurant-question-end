from django.urls import path
from . import views

urlpatterns=[
  path('staff-menu/', views.staff_menu, name='staff-menu'),

  path('staff-menu/all-orders/', views.all_orders, name='all-orders'),
  path('orders/<int:order_id>/mark-as-delivered', views.mark_as_delivered, name='mark-as-delivered'),

  path('staff-menu/all-categories/', views.all_categories, name='all-categories'),
  path('create-category/', views.create_category, name='create-category'),
  path('new-category/', views.new_category, name='new-category'),
  path('categories/<int:category_id>/edit', views.edit_category, name='edit-category'),
  path('categories/<int:category_id>/update', views.update_category, name='update-category'),
  path('categories/<int:category_id>/delete', views.delete_category, name='delete-category'),

  path('staff-menu/all-dishes/', views.all_dishes, name='all-dishes'),
  path('create-dish/', views.create_dish, name='create-dish'),
  path('new-dish/', views.new_dish, name='new-dish'),
  path('dishes/<int:dish_id>/edit', views.edit_dish, name='edit-dish'),
  path('dishes/<int:dish_id>/update', views.update_dish, name='update-dish'),
  path('dishes/<int:dish_id>/delete', views.delete_dish, name='delete-dish'),
]

