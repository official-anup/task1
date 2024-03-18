from django.urls import path
from demoapp import views

urlpatterns = [
    path('books/', views.BookListAPIView.as_view(), name='book-list'),

     path('books/id/<int:id>/', views.BookDetailAPIView.as_view(), name='book-detail'),

    path('books/language/<str:language_code>/', views.LanguageBooksAPIView.as_view(), name='language-books'),

    path('books/mime-type/<str:mime_type>/', views.MimeBooksAPIView.as_view(), name='mime-books'),


    path('books/topic/<str:topic>/', views.TopicBooksAPIView.as_view(), name='topic-books'),


      path('books/author/<str:author_name>/', views.AuthorBooksAPIView.as_view(), name='author-books'),
      
    path('books/title/<str:title>/', views.TitleBooksAPIView.as_view(), name='title-books'),

]
