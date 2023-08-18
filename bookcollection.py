"""BookCollection class."""
import csv
from operator import attrgetter

from book import Book

TITLE_POSITION = 0
AUTHOR_POSITION = 1
PAGE_POSITION = 2
REQUIRE_POSITION = 3
SORT_PRIORITY = "title"


class BookCollection:
    """Represent a BookCollection object."""

    def __init__(self):
        """Initialize a BookCollection."""
        self.books = []

    def load_books(self, filename):
        """Load books into Book objects in the list from the file passed in."""
        with open(filename, "r") as in_file:
            csv_reader = csv.reader(in_file)
            for row in csv_reader:
                if row[REQUIRE_POSITION] == "r":
                    is_completed = False
                else:
                    is_completed = True
                load_book = Book(row[TITLE_POSITION], row[AUTHOR_POSITION], int(row[PAGE_POSITION]), is_completed)
                self.books.append(load_book)

    def add_book(self, book):
        """Add a new Book object to the books attribute."""
        self.books.append(book)

    def sort(self, sort_key):
        """Sort books by the sort type passed in."""
        self.books.sort(key=attrgetter(sort_key, SORT_PRIORITY))

    def get_required_pages(self):
        """Get number of required pages."""
        required_page = 0
        for book in self.books:
            if not book.is_completed:
                required_page += book.number_of_pages
        return required_page

    def save_books(self, filename):
        """Save book information into file given."""
        book_file = open(filename, "w")
        book_information = ""
        for book in self.books:
            book_information += book.title + "," + book.author + "," + str(book.number_of_pages) + ","
            if book.is_completed:
                book_information += "c\n"
            else:
                book_information += "r\n"
        book_file.write(book_information)
        book_file.close()

    def __str__(self):
        """Return a string representation of a BookCollection object."""
        return_message = f"There are {len(self.books)} books in the collection. They are:"
        for i, book in enumerate(self.books):
            return_message += f"\n{i + 1}. {book}"
        return return_message
