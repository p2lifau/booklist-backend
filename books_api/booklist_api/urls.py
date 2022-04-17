from django.urls import path
from . import views

urlpatterns = [
    # api/contacts will be routed to the ContactList view for handling
    path('api/books', views.BookList.as_view(), name='book_list'),
    # api/contacts will be routed to the ContactDetail view for handling
    path('api/books/<int:pk>',
         views.BookDetail.as_view(), name='book_detail'),
]
