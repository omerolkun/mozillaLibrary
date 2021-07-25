from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.shortcuts import get_object_or_404

def index(request):
    """View function for home page of site."""
    booki = Book.objects.all()
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'omerbook':booki,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)
def beg127(request):
    return render(request, 'catalog/beg127_page.html')
'''

def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'catalog/book_detail.html', context={'book': book})

'''

class BookListView(generic.ListView):
    model = Book # book_janki

    context_object_name = 'omercik_book_list'
    #queryset = Book.objects.all()
    template_name  = 'catalog/book_list.html'
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/authors_list.html'

class AuthorDetaielView(generic.DetailView):
    model = Author
    template_name = 'catalog/authorie_detail.html'