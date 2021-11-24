from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="library-home"),
    path('library/', views.home, name="library-home")
]