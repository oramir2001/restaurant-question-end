from django.urls import path
from . import views

urlpatterns=[
  path('staff-homepage/', views.staff_homepage, name='staff-homepage'),
  path('staff-login/', views.staff_login, name='staff-login'),
  path('staff-menu/', views.staff_menu, name='staff-menu'),
  path('staff-menu/all-orders/', views.all_orders, name='all-orders'),
  path('staff-menu/all-categories/', views.all_categories, name='all-categories'),
  path('staff-menu/all-dishes/', views.all_dishes, name='all-dishes'),
]
# path('staff-homepage/', views.staff_homepage,name="staff-homepage"),
# path('signup_staff/',views.signup_staff,name="signup_staff")
