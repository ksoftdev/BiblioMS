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
        '/api/books/update/<id>/',
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


@api_view(['POST'])
def createBook(request):
    data = request.data

    aid = Author.objects.get(author_id=int(data['author_id']))
    cid = CategoryDetails.objects.get(category_id=int(data['category_id']))

    book = BookDetails.objects.create(
        ISBN=data['isbn'],
        book_title=data['book_title'],
        image='',
        publication_year=data['publication_year'],
        language=data['language'],
        sale_price=data['sale_price'],
        quantity_for_sale=data['quantity_for_sale'],
        author_id=aid,
        category_id=cid
    )

    book.save()

    serializer = BookDetailsSerializer(book, many=False)
    return Response(serializer.data)


@ api_view(['GET'])
def getAuthors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)

    return Response(serializer.data)


@ api_view(['GET'])
def getAuthor(request, pk):
    author = Author.objects.get(author_id=pk)
    serializer = AuthorSerializer(author, many=False)

    return Response(serializer.data)


@ api_view(['POST'])
def createAuthor(request):
    data = request.data

    author = Author.objects.create(
        author_name=data['author_name'],
        author_surname=data['author_surname']
    )

    serializer = AuthorSerializer(author, many=False)
    return Response(serializer.data)


@ api_view(['GET'])
def getCategories(request):
    categories = CategoryDetails.objects.all()
    serializer = CategoryDetailsSerializer(categories, many=True)

    return Response(serializer.data)


@ api_view(['POST'])
def createCategory(request):
    data = request.data

    category = CategoryDetails.objects.create(
        category_name=data['category_name'],
    )

    serializer = CategoryDetailsSerializer(category, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def deleteBook(request, pk):
    book = BookDetails.objects.get(book_id=pk)
    book.delete()
    return Response('The item was deleted successfully')


@api_view(['PUT'])
# @permission_classes([IsAdminUser])
def updateBook(request, pk):
    data = request.data
    book = BookDetails.objects.get(book_id=pk)

    aid = Author.objects.get(author_id=int(data['author_id']))
    cid = CategoryDetails.objects.get(category_id=int(data['category_id']))

    book.ISBN = data['isbn']
    book.book_title = data['book_title']
    book.image = data['image']
    book.publication_year = data['publication_year']
    book.language = data['language']
    book.sale_price = data['sale_price']
    book.quantity_for_sale = data['quantity_for_sale']
    book.author_id = aid
    book.category_id = cid

    book.save()

    serializer = BookDetailsSerializer(book, many=False)
    return Response(serializer.data)
