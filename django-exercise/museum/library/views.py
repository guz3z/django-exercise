from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Library</h1>")

def library(request):
    return HttpResponse("<h1>This is the library page</h1>")

def books(request):
    return HttpResponse(
        "<h1>These are all our books</h1>"
        f"<p>We have {len(books)} books in our library</p>"
    )
