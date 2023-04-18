from django.urls import path
from . import views

urlpatterns=[
  path('',views.homepage,name="homepage"),
  path('login/',views.login_user,name="login"),
  path('logout',views.logout,name="logout"),
  path('signup/',views.signup,name="signup"),
  path('user/',views.show_account,name="show_account"),
  path('starters/',views.starters,name="starters_dished"),
  path('mains',views.mains,name="main_dishes"),
  path('desserts',views.desserts,name="desserts_menu"),
  path('drinks',views.drinks,name="drinks_menu")
]
