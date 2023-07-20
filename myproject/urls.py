"""
URL configuration for catalog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from HW12.views import BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView, author_books, \
    author_list, \
    publisher_books, publisher_list, store_detail, store_list

from celery_task.views import create_reminder

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from triangle.views import person_add, person_edit, person_list, triangle_view

app_name = 'triangle'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('triangle/', triangle_view, name='triangle'),
    path('person/add', person_add, name='person_add'),
    path('person/edit/<int:pk>/', person_edit, name='person_edit'),
    path('person/list/', person_list, name='person_list'),
]
app_name = 'celery_task'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-reminder/', create_reminder, name='create_reminder'),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

app_name = 'HW12'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', author_list, name='author_list'),
    path('author/<int:pk>/', author_books, name='author_books'),
    path('publishers/', publisher_list, name='publisher_list'),
    path('publisher/<int:pk>/books/', publisher_books, name='publisher_books'),
    # path('books/', book_list, name='book_list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('edit/<int:pk>/', BookUpdateView.as_view(), name='book-edit'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    # path('book/<int:pk>/', book_detail, name='book_detail'),
    path('stores/', store_list, name='store_list'),
    path('store/<int:pk>/', store_detail, name='store_detail'),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
