from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),

    path('books/', views.getBooks, name="books"),
    path('books/<str:pk>', views.getBook, name="book"),

    path('authors/', views.getAuthors, name="authors"),
    path('authors/<str:pk>', views.getAuthor, name="author"),

    path('categories/', views.getCategories, name="categories"),
]
