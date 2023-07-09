from HW12.models import Author, Book, Publisher, Store

from django.db.models import Avg, Count, Sum
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def author_list(request):
    authors = Author.objects.annotate(num_books=Count('book')).prefetch_related('book_set')
    context = {'authors': authors}
    return render(request, 'author_list.html', context)


def author_books(request, pk):
    author = get_object_or_404(Author.objects.prefetch_related('book_set'), pk=pk)
    books = author.book_set.all()
    context = {'author': author, 'books': books}
    return render(request, 'author_books.html', context)


def publisher_list(request):
    publishers = Publisher.objects.annotate(
        num_books=Count('book'),
        total_pages=Sum('book__pages')
    ).prefetch_related('book_set')

    context = {'publishers': publishers}
    return render(request, 'publisher_list.html', context)


def publisher_books(request, pk):
    publisher = get_object_or_404(Publisher.objects.prefetch_related('book_set'), pk=pk)
    books = publisher.book_set.all()

    context = {'publisher': publisher, 'books': books}
    return render(request, 'publisher_books.html', context)


def book_list(request):
    books = Book.objects.all().prefetch_related('authors')

    average_pages = books.aggregate(avg_pages=Avg('pages'))
    average_price = books.aggregate(avg_price=Avg('price'))
    average_rating = books.aggregate(avg_rating=Avg('rating'))

    context = {
        'books': books,
        'average_pages': average_pages,
        'average_price': average_price,
        'average_rating': average_rating
    }
    return render(request, 'book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(
        Book.objects.prefetch_related('store_set').select_related('publisher'),
        pk=pk
    )
    books = [book]
    context = {'books': books}
    return render(request, 'book_detail.html', context)


def store_list(request):
    stores = Store.objects.annotate(num_books=Count('books')).prefetch_related('books')
    context = {'stores': stores}
    return render(request, 'store_list.html', context)


def store_detail(request, pk):
    store = get_object_or_404(Store.objects.prefetch_related('books'), pk=pk)
    books = store.books.all()
    context = {
        'store': store,
        'books': books
    }
    return render(request, 'store_detail.html', context)
# Create your views here.
