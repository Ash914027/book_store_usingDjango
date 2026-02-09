from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_detail'),
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
]