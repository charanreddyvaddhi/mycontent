from django.urls import path, include, re_path
from .import views
urlpatterns=[
    path('', views.index, name='index'),  #path for home page
    path('books/', views.BookListView.as_view(),name='books'), #path for getting list of books
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), #path for getting details of book
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'), #path for getting details of book
    path('authors/',views.AuthorListView.as_view(), name='authors'), #path for getting list of authors books in library
    #path('authors/',views.authors,name='authors')  #path for getting list of authors books in library
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]