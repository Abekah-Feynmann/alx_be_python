class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"{self.title} has been returned successfully"
        else:
            return f"{self.title} was not checked out"

class Library: 
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    return f"{book.title} is unavailable"
                else:
                    book._is_checked_out = True
                    return f"{book.title} is successfully checked out"
        return f"{title} is not available in the library"

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f"{title} was not found in the library"
    
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book)


        
