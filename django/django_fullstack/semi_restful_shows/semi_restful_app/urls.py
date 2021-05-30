from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.create),
    path('shows/create', views.create_object),
    path('shows/<int:id>', views.render_create),
    path('<int:id>/edit', views.edit)
]
