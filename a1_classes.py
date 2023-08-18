"""Reading tracker program."""

import csv
from operator import attrgetter

from book import Book

TITLE_POSITION = 0
AUTHOR_POSITION = 1
PAGE_POSITION = 2
REQUIRE_POSITION = 3

MINIMUM_PAGE_NUMBER = 0
TYPES_OF_BOOK_DETAIL = 4
FILENAME = "books.csv"


def main():
    """Start of reading tracker program."""
    books = load_book_list(FILENAME)  # Load the book file to a list
    books.sort(key=attrgetter("author", "title"))

    print("Reading Tracker 1.0 - by Tianyi Zhang")
    print(f"{len(books)} books loaded")

    choice = input("Menu: \nL - List all books\nA - Add new book\n"
                   "M - Mark a book as completed\nQ - Quit\n>>> ").upper()
    while choice != "Q":
        if choice == "L":
            display_book(books)  # List all book information
            display_pages_left_to_read(books)
        elif choice == "M":  # Let user mark book as completed if there is any required book
            if count_required_book(books) == 0:
                print("No required books")
            else:
                display_book(books)
                display_pages_left_to_read(books)
                print("Enter the number of a book to mark as completed")
                marked_book = int(handle_book_number_input(">>>", books))  # Get which book to mark
                mark_book(books[marked_book - 1])
        elif choice == "A":
            new_book = get_book()
            books.append(new_book)
            display_added_message(new_book)
        else:
            print("Invalid menu choice")
        choice = input("Menu: \nL - List all books\nA - Add new book\n"
                       "M - Mark a book as completed\nQ - Quit\n>>> ").upper()
    display_farewell_message(books)
    save_book_information(books)


def mark_book(book):
    """Mark a book as completed if it is not completed."""
    if not determine_book_state(book):  # Check if that book is completed
        print("That book is already completed")
    else:
        display_marked_message(book)
        book.mark_completed()


def display_marked_message(book):
    """Display the book is completed after mark the book."""
    print(f"{book.title} by "
          f"{book.author} completed!")


def display_farewell_message(books):
    """Display farewell messages after user quit."""
    print(f"{len(books)} books saved to books.csv")
    print("So many books, so little time. Frank Zappa")


def save_book_information(books):
    """Save all book information into file."""
    out_file = open(FILENAME, "w")
    book_information = ""
    for book in books:
        book_details = [book.title, book.author, str(book.number_of_pages)]
        if book.is_completed:
            book_details.append("c")
        else:
            book_details.append("r")
        book_information += ",".join(book_details)  # Put comma between words
        book_information += "\n"
    out_file.write(book_information)
    out_file.close()


def get_book():
    """Get new book details from user."""
    title = handle_text_input("Title:")
    author = handle_text_input("Author:")
    pages = int(handle_page_input("Pages:"))
    new_book = Book(title, author, pages, False)
    return new_book


def display_added_message(book):
    """Display book added message."""
    title = book.title
    author = book.author
    pages = book.number_of_pages
    print(f"{title} by {author}, ({pages} pages) added to Reading Tracker")


def handle_text_input(input_name):
    """Handle text inputs with exception."""
    is_valid_input = False
    input_value = None
    while not is_valid_input:
        try:
            input_value = input(f"{input_name} ")
            if input_value == "":
                raise ValueError
            is_valid_input = True
        except ValueError:
            print("Input can not be blank")
    return input_value


def handle_page_input(input_name):
    """Handle page input with exception."""
    is_valid_input = False
    input_value = None
    while not is_valid_input:
        try:
            input_value = input(f"{input_name} ")
            if input_value == "":
                raise ValueError
            elif int(input_value) <= MINIMUM_PAGE_NUMBER:
                print("Number must be > 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return input_value


def handle_book_number_input(input_name, books):
    """Handle book number input with exception."""
    is_valid_input = False
    input_value = None
    while not is_valid_input:
        try:
            input_value = input(f"{input_name} ")
            if int(input_value) <= 0:
                print("Number must be > 0")
            elif int(input_value) > len(books):
                raise IndexError
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
        except IndexError:
            print("Invalid book number")
    return input_value


def load_book_list(book_file):
    """Load books from the file into Book objects in a list."""
    books = []
    with open(book_file, "r") as in_file:
        csv_reader = csv.reader(in_file)
        for row in csv_reader:
            if row[REQUIRE_POSITION] == "r":
                is_completed = False
            else:
                is_completed = True
            load_book = Book(row[TITLE_POSITION], row[AUTHOR_POSITION], int(row[PAGE_POSITION]), is_completed)
            books.append(load_book)
    return books


def display_book(books):
    """Display books in the book list."""
    for i, book in enumerate(books):
        star = determine_star_state(book)  # Add star if the book is required
        print(f"{star}{i + 1}. {book}")


def count_required_book(books):
    """Count the number of required books left."""
    required_book = 0
    for book in books:
        if determine_book_state(book):
            required_book += 1
    return required_book


def count_pages_left(books):
    """Count the number of pages left to read."""
    page_number = 0
    for book in books:
        if determine_book_state(book):
            page_number += book.number_of_pages
    return page_number


def display_pages_left_to_read(books):
    """Display number of page and book left to read."""
    page_number = count_pages_left(books)
    required_book = count_required_book(books)
    if required_book > 0:
        print(f"You need to read {page_number} pages in {required_book} books.")
    else:
        print("No books left to read. Why not add a new book?")


def determine_star_state(book):
    """Return "*" if the book is required."""
    star = " "
    if determine_book_state(book):
        star = "*"
    return star


def determine_book_state(book):
    """Determine whether the book is required."""
    return not book.is_completed


if __name__ == '__main__':
    main()
