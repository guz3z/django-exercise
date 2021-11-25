from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="museum-home"),
    path('books/', views.books, name="library-books"),
    path('books/<int:id>/', views.show, name="library-show")
]