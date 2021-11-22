from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),

    path('books/', views.getBooks, name="books"),
    path('books/<str:pk>', views.getBook, name="book"),

    path('books/create/', views.createBook, name="create-book"),

    path('authors/', views.getAuthors, name="authors"),
    path('authors/<str:pk>', views.getAuthor, name="author"),

    path('authors/create/', views.createAuthor, name="create-author"),

    path('categories/', views.getCategories, name="categories"),

    path('categories/create/', views.createCategory, name="create-category"),

    path('books/delete/<str:pk>/', views.deleteBook, name="delete-book"),

    path('books/update/<str:pk>/', views.updateBook, name="update-book"),
]
