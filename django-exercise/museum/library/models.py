from django.db import models

# Create your models here.
all_books = [
    {"id": 1, "title": "Emotional Intelligence", "author": "Daniel Goleman"},
    {"id": 2, "title": "The 48 laws of power", "author": "Robert Greene"},
    {"id": 3, "title": "Rich dad poor dad", "author": "Robert Kiyosaki"},
]

# class Book(models.Model):
#     title = models.CharField(max_length=150)
#     author = models.CharField(max_length=60)

#     def __str__(self):
#         return self.title
