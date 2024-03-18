from rest_framework import serializers
from .models import (
    BooksBook, BooksAuthor, BooksLanguage,
    BooksSubject, BooksFormat
)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = BooksBook
        fields = ['id', 'title', 'download_count', 'media_type', 'authors']



REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}