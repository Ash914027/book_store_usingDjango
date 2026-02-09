from django.shortcuts import render

from .models import CartItem
from django.shortcuts import get_object_or_404, redirect
from catalog.models import Book
# Create your views here.
def cart_view(request):
    # Logic to display the user's cart
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})
def add_to_cart(request, book_id):
    # Logic to add a book to the cart
    book = get_object_or_404(Book, id=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

def checkout_view(request):
    # Placeholder for checkout logic
    return render(request, 'cart/checkout.html')