from django.urls import path
from . import views

urlpatterns=[
  path('',views.homepage,name="homepage"),
  path('login/',views.login_user,name="login"),
  path('logout',views.logout,name="logout"),
  path('signup/',views.signup,name="signup"),
  path('menu/',views.menu,name="menu"),
  path('menu/show-dishes/<int:id>/',views.show_dishes,name="show-dishes"),
  path('menu/cart/',views.cart,name="my-cart"),
  path('menu/add-dish-to-cart/',views.add_dish_to_cart,name="add-dish-to-cart"),
  path('menu/remove-dish-from-cart',views.remove_dish_from_cart,name="remove-dish-from-cart"),
  path('menu/checkout/',views.checkout,name="checkout"),
  path('submit-order/',views.submit_order,name="submit-order"),
  path('menu/thank-you/',views.thank_you,name="thank-you"),
  path('menu/orders/',views.orders,name="orders"),
  path('change-details/',views.change_details,name="change-details"),
]
