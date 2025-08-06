from django.urls import path
<<<<<<< HEAD
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)
=======
from .views import BookListView, BookDetailView
from . import views
>>>>>>> f2382b6baa6435a311c316d541563b2245312faf

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('add/', BookCreateView.as_view(), name='book_add'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]

