from rest_framework import serializers
from .models import BookDetails, CategoryDetails, Author


class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'


class CategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDetails
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
