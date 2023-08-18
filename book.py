"""Represent a Book object."""
LONG_BOOK_PAGE_NUMBER = 500


class Book:
    """Represent a Book object."""

    def __init__(self, title="", author="", number_of_pages=0, is_completed=False):
        """Initialise a BookCollection."""
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_completed = is_completed

    def mark_required(self):
        """Mark the book to require."""
        self.is_completed = False

    def mark_completed(self):
        """Mark the book to complete."""
        self.is_completed = True

    def is_long(self):
        """Determine if a book is long (>500 pages)."""
        return self.number_of_pages > LONG_BOOK_PAGE_NUMBER

    def handle_state_message(self):
        """Return (completed) if the book is completed or blank if the book is required."""
        state_message = ""
        if self.is_completed:
            state_message = "(completed)"
        return state_message

    def __str__(self):
        """Return a string representation of a Book object."""
        return f"{self.title} by {self.author}, {self.number_of_pages} pages {self.handle_state_message()}"
