  
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('books',views.welcome),
    path('logout',views.logout),
    path('login',views.login),
    path('add_book', views.add_book),
    path('books/<int:book_id>' ,views.book_details),
    path('books/add_to_fav/<int:book_id>',views.add_to_fav),
    path('books/<int:book_id>/destroy', views.del_book),
    path('books/<int:book_id>/update', views.update_book),

]