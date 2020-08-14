from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_orders, name='all_orders'),
    path('cart', views.cart, name='cart'),
    path('addToCart/<int:item_id>/', views.addToCart, name='additem'),
    path('checkout/<int:chain>/', views.checkout, name='checkout')
]
