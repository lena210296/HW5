from HW12.models import Author, Book, Publisher, Store

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Avg, Count, Sum
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# from django.urls import reverse_lazy
# from django.views.generic import (
#    CreateView,
#    DeleteView,
#   DetailView,
#   ListView,
#   UpdateView,

# )

# from .forms import BookForm

@cache_page(60 * 2)
def author_list(request):
    authors = Author.objects.annotate(num_books=Count('book')).prefetch_related('book_set')
    paginator = Paginator(authors, 100)
    page = request.GET.get('page')
    try:
        paginated_authors = paginator.page(page)
    except PageNotAnInteger:

        paginated_authors = paginator.page(1)
    except EmptyPage:

        paginated_authors = paginator.page(paginator.num_pages)

    context = {'paginated_authors': paginated_authors}
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


@cache_page(60 * 2)
def book_list(request):
    books = Book.objects.all().prefetch_related('authors')

    paginator = Paginator(books, 100)
    page = request.GET.get('page')

    try:
        paginated_books = paginator.page(page)
    except PageNotAnInteger:

        paginated_books = paginator.page(1)
    except EmptyPage:

        paginated_books = paginator.page(paginator.num_pages)

    average_pages = books.aggregate(avg_pages=Avg('pages'))
    average_price = books.aggregate(avg_price=Avg('price'))
    average_rating = books.aggregate(avg_rating=Avg('rating'))

    context = {
        'average_pages': average_pages,
        'average_price': average_price,
        'average_rating': average_rating,
        'paginated_books': paginated_books,
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


"""
class BookListView(ListView):
    model = Book
    template_name = 'book_list_new.html'
    paginate_by = 10


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book_detail_new.html'
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['rating'].widget.attrs['step'] = '0.01'
        form.fields['pubdate'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        return form


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['rating'].widget.attrs['step'] = '0.01'
        form.fields['pubdate'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        return form


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

"""


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
