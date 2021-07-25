from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexOmercik'),
    path('books/',views.BookListView.as_view(), name = "bsooks"),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/',views.AuthorListView.as_view(),name='authors_genc'),
    path('authors/<int:pk>', views.AuthorDetaielView.as_view(), name='author-detail'),


]