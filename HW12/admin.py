from HW12.models import Author, Book, Publisher, Store

from django.contrib import admin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name',)
    list_filter = ('age',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price', 'rating', 'pubdate', 'publisher')
    list_filter = ('rating', 'publisher')
    search_fields = ('name', 'publisher__name')
    filter_vertical = ('authors',)
    date_hierarchy = 'pubdate'


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_vertical = ('books',)
