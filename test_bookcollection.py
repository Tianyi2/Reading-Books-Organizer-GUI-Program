"""(Incomplete) Tests for BookCollection class."""
from book import Book
from bookcollection import BookCollection


def run_tests():
    """Test BookCollection class."""

    # Test empty BookCollection (defaults)
    print("Test empty BookCollection:")
    book_collection = BookCollection()
    print(book_collection)
    assert not book_collection.books  # PEP 8 suggests not using len() to test for empty lists
    print()

    # Test loading books
    print("Test loading books:")
    book_collection.load_books('books.csv')
    print(book_collection)
    assert book_collection.books  # assuming CSV file is non-empty, length should be non-zero
    print()

    # Test adding a new Book with values
    print("Test adding new book:")
    print("Expect the book collection have 5 books")
    book_collection.add_book(Book("War and Peace", "William Shakespeare", 999, False))
    print(book_collection)
    print()

    # Test sorting books
    print("Test sorting - author:")
    book_collection.sort("author")
    print(book_collection)
    print()

    print("Test sorting - title:")
    book_collection.sort("title")
    print(book_collection)
    print()

    print("Test sorting - page number:")
    book_collection.sort("number_of_pages")
    print(book_collection)
    print()

    print("Test sorting - state:")
    book_collection.sort("is_completed")
    print(book_collection)
    print()

    # Test getting required number of pages
    print("Test get_required_pages():")
    new_book_collection = BookCollection()
    new_book_collection.load_books("books.csv")
    print(f"Expected result: 594   Actual results: {new_book_collection.get_required_pages()}")
    print()

    # Test saving books (check CSV file manually to see results)
    print("Test saving books:\nCheck CSV file manually to see results")
    book_collection.save_books("books.csv")
    print()

    # Test getting required number of pages when added a new book
    print("Test get_required_pages() when added a new book:")
    new_book_collection.add_book(Book("Hello World", "Tommy", 1, False))
    print(f"Expected result: 595   Actual results: {new_book_collection.get_required_pages()}")


run_tests()
