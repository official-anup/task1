from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import BooksBook
from .serializers import BookSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = BooksBook.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id' 

    def get_queryset(self):
        queryset = BooksBook.objects.all()
        filters = self.request.query_params
        if 'language' in filters:
            queryset = queryset.filter(languages__code=filters['language'])
        if 'topic' in filters:
            queryset = queryset.filter(subjects__name__icontains=filters['topic'])
        if 'author' in filters:
            queryset = queryset.filter(authors__name__icontains=filters['author'])
        return queryset.order_by('-download_count')[:20]


class LanguageBooksAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = BooksBook.objects.all()
        language_code = self.kwargs.get('language_code')

        if language_code:
            queryset = queryset.filter(language_code=language_code)

        return queryset.order_by('-download_count')[:20]
    

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = BooksBook.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'



class MimeBooksAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        mime_type = self.kwargs['mime_type']
        return BooksBook.objects.filter(mime_type=mime_type).order_by('-download_count')[:20]
    
class TopicBooksAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        topic = self.kwargs['topic']
        return BooksBook.objects.filter(subjects__name__icontains=topic).order_by('-download_count')[:20]

class AuthorBooksAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = BooksBook.objects.all()
        author_name = self.kwargs.get('author_name')

        if author_name:
            queryset = queryset.filter(book_authors__name__icontains=author_name)

        return queryset.order_by('-download_count')[:20]
    

    
class TitleBooksAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = BooksBook.objects.all()
        title = self.kwargs.get('title')

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset.order_by('-download_count')[:20]