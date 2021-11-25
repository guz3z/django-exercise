from django.shortcuts import render
from django.http import HttpResponse
from .models import all_books

# Create your views here.
def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, './404.html', data)

def server_error_500(request):
    return render(request, './500.html')


def homepage(request):
    return render(request, 'base.html')

def books(request):
    return render(request, 'home.html')

# def show(request, id):
#     # book = list(filter(lambda books: books['id'] == id, all_books))
#     # return HttpResponse(
#     #     f"<h1>This page is for book number: {id}</h1>"
#     #     f"<p>The title of this book is {book[0]['title']}.</p>"
#     #     f"<p>The author of this book is {book[0]['author']}</p>"
#     # )