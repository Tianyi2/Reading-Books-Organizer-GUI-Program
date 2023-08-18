"""Tests for Book class."""
from book import Book


def run_tests():
    """Test Book class."""

    # Test empty book (defaults)
    print("Test empty book:")
    default_book = Book()
    print(default_book)
    assert default_book.title == ""
    assert default_book.author == ""
    assert default_book.number_of_pages == 0
    assert not default_book.is_completed
    print()

    # Test initial-value book
    print("Test initial-value book:")
    new_book = Book("Fish Fingers", "Dory", 501, True)
    print(f"Expected result: Fish Fingers  Actual results: {new_book.title}")
    print(f"Expected result: Dory          Actual results: {new_book.author}")
    print(f"Expected result: 501           Actual results: {new_book.number_of_pages}")
    print(f"Expected result: True          Actual results: {new_book.is_completed}")
    print()

    # Test mark_required()
    print("Test mark_required():")
    new_book.mark_required()
    print(f"Expected result: False         Actual results: {new_book.is_completed}")
    print()

    # Test is_long()
    print("Test is_long():")
    print(f"{new_book.title} has {new_book.number_of_pages} pages. Is it long?: ")
    print(f"Expected result: True         Actual results: {new_book.is_long()}")

    second_book = Book("Ege and Chicken", "Tom", 499, True)
    print(f"{second_book.title} has {second_book.number_of_pages} pages. Is it long?: ")
    print(f"Expected result: False        Actual results: {second_book.is_long()}")
    print()

    # Test mark_completed()
    print("Test mark_completed():")
    new_book.mark_completed()
    print(f"Expected result: True        Actual results: {new_book.is_completed}")
    print()

    # Test str method
    print("Test str method:")
    print(new_book)


run_tests()
