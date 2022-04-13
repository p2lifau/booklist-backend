from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book


class BookList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer  # tell django what serializer to use


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
