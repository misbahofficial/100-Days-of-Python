# List of dictionaries representing books
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

# Using lambda function to sort books by year
sorted_books_by_year = sorted(books, key=lambda book: book["year"])

# Using lambda function to sort books by title length
sorted_books_by_title_length = sorted(books, key=lambda book: len(book["title"]))

print("Original List of Books:", books)
print("Books Sorted by Year:", sorted_books_by_year)
print("Books Sorted by Title Length:", sorted_books_by_title_length)