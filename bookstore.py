#   Create an online bookstore inventory system using object-oriented programming principles. The system should allow you to manage a collection of books. Each of the books should have its own attributes e.g. title, author, genre, price, and quantity available.​

class BookStore:

    def __init__(self,books):
        if books:
            self.books = books
        else:
            self.books = {}
    
    def add_book(self,title, author, genre, price, quantity):
        self.books[title] = {'author':author,'genre':genre,'price':price,'quantity':quantity}
    
    def sell_book(self,title,quantity):
        if title in self.books:
            if self.books[title]['quantity'] >= quantity:
                self.books[title]['quantity'] -= quantity
                return True
            else:
                return False
        else:
            return False

    def price_of_transaction(self,title,quantity):
        print("\nTransaction Details:")
        if title in self.books and self.sell_book(title,quantity):
            print(f"Sold {str(quantity)} {title} for ${self.books[title]['price'] * quantity}")
        else:
            print("not enough books in stock")
        
    def count_books(self):
        print("\nBook Inventory:")
        for book in self.books:
            print(book,self.books[book]['quantity'])

rahuals_bookstore = BookStore({"Book A":{'author':'Rahul','genre':'Fantasy','price':10,'quantity':10}, "Book B":{'author':'Aaryan','genre':'Fantasy','price':12,'quantity':20}})
rahuals_bookstore.add_book('Book C','Niya','Non-Fiction',10,15)
rahuals_bookstore.count_books()
rahuals_bookstore.price_of_transaction('Book C',2)
rahuals_bookstore.count_books()
    