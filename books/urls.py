from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('books', views.books, name="books"),
    path('add_books', views.add_books, name="add_books"),
    path('delete/<book_id>', views.delete, name="delete"),
    path('edit/<book_id>', views.edit, name="edit"),
    path('update/<book_id>', views.update, name="update"),
    path('import_books', views.import_books, name="import_books"),
    path('list_book', views.BookPurchaseList.as_view(), name="list_book"),
]
