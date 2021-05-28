from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('books/<int:id>', views.showBook),
    path('books/addAuthorToBook/<int:book_id>', views.addAuthorToBook),
    path('authors', views.authorHome),
    path('authors/<int:id>', views.showAuthor),
    path('addAuthor', views.addAuthor),
    # path('addBook/<author_id>', views.addAuthor),
]
