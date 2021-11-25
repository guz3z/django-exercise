from django.shortcuts import render
from django.http import HttpResponse
from .models import all_books

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Library</h1>")

def books(request):
    return HttpResponse(
        "<h1>These are all our books:</h1>"
        f"<p>{all_books}</p>"
    )

def show(request, id):
    book = list(filter(lambda books: books['id'] == id, all_books))
    return HttpResponse(
        f"<h1>This page is for book number: {id}</h1>"
        f"<p>The title of this book is {book[0]['title']}.</p>"
        f"<p>The author of this book is {book[0]['author']}</p>"
    )