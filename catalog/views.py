from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404



def book_list(request):
    # Logic to retrieve and display a list of books
    books = Book.objects.all()
    return render(request, 'catalog/booklist.html', {'books': books})
def book_detail(request, book_id):
    # Logic to retrieve and display details of a specific book
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'catalog/bookdetail.html', {'book': book})
