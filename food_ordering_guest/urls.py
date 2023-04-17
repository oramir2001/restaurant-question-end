from django.urls import path
from . import views

urlpatterns=[
  path('',views.homepage,name="homepage"),
  path('login/',views.login_user,name="login"),
  path('logout',views.logout,name="logout"),
  path('signup/',views.signup,name="signup"),
  path('user/',views.show_account,name="show_account")
]
