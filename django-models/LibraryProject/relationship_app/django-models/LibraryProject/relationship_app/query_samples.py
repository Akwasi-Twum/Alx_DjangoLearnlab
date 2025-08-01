import os
import django

# Setup Django environment (adjust path if needed)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(ForeignKey):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(ForeignKey)
        books = author.books.all()
        print(f"Books by {ForeignKey}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {ForeignKey}")

def list_books_in_library(ManyToManyField):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=ManyToManyField)
        books = library.books.all()
        print(f"Books in library '{ManyToManyField}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name: {ManyToManyField}")

def get_librarian_for_library(OneToOneField):
    """Retrieve the librarian for a specific library."""
    try:
        library = Library.objects.get(name=OneToOneField)
        librarian = library.librarian
        print(f"Librarian for library '{OneToOneField}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {OneToOneField}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{OneToOneField}'.")

