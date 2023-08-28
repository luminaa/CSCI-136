"""
Create an online bookstore inventory system using object-oriented programming.
The system should allow you to manage a collection of books. 
Each of the books should have its own attributes e.g. title, author, genre, price, and quantity available
"""

class Book:
    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

    def purchase(self, number):
        if self.quantity >= number:
            self.quantity -= number
            return True
        else:
            return False

class Customer:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.purchased_books = {}

    def purchase_book(self, book, number):
        if book.purchase(number):
            self.purchased_books[book.title] = self.purchased_books.get(book.title, 0) + number
            print(f"\nThank you, {self.first_name}! You have purchased {number} of '{book.title}'.")
        else:
            print(f"\nSorry, only {book.quantity} of '{book.title}' is available.")

    def show_purchased_books(self):
        if not self.purchased_books:
            print(f"\n{self.first_name} hasn't purchased any books yet.")
            return
        print(f"\nBooks purchased by {self.first_name} {self.last_name}:")
        for book, quantity in self.purchased_books.items():
            print(f"- {quantity}x {book}")


class BookStore:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.title] = book

    def list_books(self):
        print("\nBooks Available:")
        for title, book in self.books.items():
            print(f"{title} by {book.author},  Genre: {book.genre},  Price: ${book.price},  Available: {book.quantity}")

    def search_by_title(self, title):
        found_books = [book for book_title, book in self.books.items() if title.lower() in book_title.lower()]
        if not found_books:
            print(f"\nNo books found with title containing '{title}'.")
            return
        print("\nBooks Found:")
        for book in found_books:
            print(book.title)


rahuals_bookstore = BookStore()
rahuals_bookstore.add_book(Book("Book A", "Rahual", "Fantasy", 10, 10))
rahuals_bookstore.add_book(Book("Book B", "Aaryan", "Fantasy", 12, 20))
rahuals_bookstore.add_book(Book("Book C", "Niya", "Non-Fiction", 10, 15))
rahuals_bookstore.list_books()
rahuals_bookstore.search_by_title("Book")

araj = Customer("Araj", "Shah", "araj.shah@gmail.com")
araj.purchase_book(rahuals_bookstore.books["Book A"], 2)
araj.purchase_book(rahuals_bookstore.books["Book B"], 3)
araj.purchase_book(rahuals_bookstore.books["Book C"], 4)
araj.show_purchased_books()

rahuals_bookstore.list_books()