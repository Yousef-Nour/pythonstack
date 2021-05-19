from django.urls import path     
from . import views
urlpatterns = [
    path('', views.count),
    # path('destroy_session', views.destroy), 
    path('destroy', views.destroy),
    path('increment', views.increment),
    path('incrementByNum', views.incrementByNum ),
]