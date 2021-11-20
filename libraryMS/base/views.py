from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .books import books
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
    return Response(books)


@api_view(['GET'])
def getBook(request, pk):
    book = None
    for b in books:
        if b['_id'] == pk:
            book = b
            break

    return Response(book)
