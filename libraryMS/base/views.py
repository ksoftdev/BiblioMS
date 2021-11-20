from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .books import books
from .models import BookDetails, CategoryDetails, Author
from .serializers import BookDetailsSerializer, AuthorSerializer, CategoryDetailsSerializer
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/books/',
        '/api/books/<id>/',
        '/api/books/create/',

        '/api/authors/',
        '/api/authors/<id>/',
        '/api/authors/create/',

        '/api/categories/',
        '/api/categories/create/',

        '/api/books/delete/<id>/',
        '/api/books/<update>/<id>/',
    ]
    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    books = BookDetails.objects.all()
    serializer = BookDetailsSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, pk):
    book = BookDetails.objects.get(book_id=pk)
    serializer = BookDetailsSerializer(book, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def getAuthors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getAuthor(request, pk):
    author = Author.objects.get(author_id=pk)
    serializer = AuthorSerializer(author, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def getCategories(request):
    categories = CategoryDetails.objects.all()
    serializer = CategoryDetailsSerializer(categories, many=True)

    return Response(serializer.data)
