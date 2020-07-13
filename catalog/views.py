from django.shortcuts import render
from catalog.models import Author, BookInstance, Book, Genre, Language
from django.views import generic
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()  # Generate counts of some of the main objects
    num_instances = BookInstance.objects.all().count()  # Generate counts of some of the main objects
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()  # Available books (status = 'a')
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(
    generic.ListView):  # That's it! The generic view will query the database to get all records for  the specified model (Book)
    model = Book
    context_object_name = 'my_book_list'  # specify the same name as my_book_list in book list.html page at if and for conditions
    # queryset = Book.objects.filter(title__icontains='The')[:5]
    queryset = Book.objects.all()
    # template_name = 'books/my_arbitrary_template_name_list.html'
    template_name = 'book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})


"""
def authors(request):
    return render (request, 'author_list.html')
"""


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'authors_list'
    queryset = Author.objects.order_by()
    template_name = 'author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
