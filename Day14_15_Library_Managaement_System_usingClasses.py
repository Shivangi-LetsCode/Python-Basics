class Book:
    # Static variable to keep track of total books
    total_books = 0

    def _init_(self, title, author, year):
        self.book_id = Book.total_books + 1
        self.title = title
        self.author = author
        self.year = year
        Book.total_books += 1

    def display(self):
        print(f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Year: {self.year}")

    @staticmethod
    def library_rules():
        print("\n📚 Library Rules:")
        print("- Keep books safe")
        print("- Return books within 15 days")
        print("- Handle with care\n")


class Library:
    def _init_(self):
        self.books = []

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        print(f" Book '{title}' added successfully.\n")

    def display_all_books(self):
        if not self.books:
            print("No books in the library.\n")
            return
        print(" Library Book List:")
        for book in self.books:
            book.display()
        print()

    def search_book(self, keyword):
        found = False
        print(f" Searching for '{keyword}':")
        for book in self.books:
            if keyword.lower() in book.title.lower():
                book.display()
                found = True
        if not found:
            print("No matching books found.\n")

    def update_book(self, book_id, new_title, new_author, new_year):
        for book in self.books:
            if book.book_id == book_id:
                book.title = new_title
                book.author = new_author
                book.year = new_year
                print(" Book updated successfully.\n")
                return
        print(" Book ID not found.\n")

    def delete_book(self, book_id):
        for i, book in enumerate(self.books):
            if book.book_id == book_id:
                del self.books[i]
                print("️ Book deleted successfully.\n")
                return
        print(" Book ID not found.\n")

    def total_books(self):
        print(f" Total books in library: {Book.total_books}\n")



lib = Library()

# Static method (class-level)
Book.library_rules()

# Add books
lib.add_book("The Alchemist", "Paulo Coelho", 1988)
lib.add_book("Rich Dad Poor Dad", "Robert Kiyosaki", 1997)
lib.add_book("Clean Code", "Robert C. Martin", 2008)


lib.display_all_books()

lib.search_book("rich")

lib.update_book(2, "Rich Dad Poor Dad", "R. Kiyosaki", 2000)

lib.delete_book(3)

lib.display_all_books()

lib.total_books()
