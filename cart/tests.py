
from django.test import TestCase
from .models import CartItem
from django.contrib.auth import get_user_model
from catalog.models import Book

class CartItemModelTest(TestCase):
	def test_create_cart_item(self):
		User = get_user_model()
		user = User.objects.create_user(username='testuser', password='testpass')
		book = Book.objects.create(title='Book', author='Author', isbn='1234567890123', price=10, stock=5)
		cart_item = CartItem.objects.create(user=user, book=book, quantity=2)
		self.assertEqual(cart_item.quantity, 2)
