
from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
	def test_create_book(self):
		book = Book.objects.create(title='Book', author='Author', isbn='1234567890123', price=10, stock=5)
		self.assertEqual(book.title, 'Book')
