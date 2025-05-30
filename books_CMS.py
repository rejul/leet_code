books = {}

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # For simplicity, using hardcoded credentials
    if username == "admin" and password == "password":
        print("Login successful\n")
        return True
    else:
        print('Invalid Credentials')
        return False







def menu():
   while True: 
    print("Welcome to the Books CMS")
    print("1. Add Book")
    print("2. View all Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        #add book
        add_book()
    elif choice == '2':
         #view book
        view_books()
    elif choice == '3':
        #update book
        update_book()
    elif choice == '4':
        #delete book
        delete_book()
    elif choice == '5':
        #search book
        search_book()
    elif choice == '6':
        print("Exiting the system")
        return
    else:
        print("Invalid choice, please try again")    


def add_book():
    book_id = input("Enter book ID: ")
    # Check if book ID already exists
    if book_id in books:
        print(f"Book with ID {book_id} already exists. Please use a different ID.\n")
        return
    print("Adding a new book")    
    #book_id= input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter publication year: ")
    copies= input("Enter number of copies: ")

    
    books[book_id] = {
        'title': title,
        'author': author,
        'year': year,
        'copies': copies

    }

    print(f"Book '{title}' added successfully with ID {book_id}\n")

def view_books():
    if not books:
        print("No books available.\n")
        return
    
    print("List of Books:")
    for book_id, info in books.items():
        print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Year: {info['year']}, Copies: {info['copies']}")
    print()


def update_book():
    book_id = input("Enter the book ID to update: ")
    
    if book_id not in books:
        print(f"No book found with ID {book_id}.\n")
        return
    
    print("Updating book details")
    title = input(f"Enter new book title - {books[book_id]['title']} (leave blank to keep current): ") or books[book_id]['title']
    author = input(f"Enter new book author - {books[book_id]['author']} (leave blank to keep current): ") or books[book_id]['author']
    year = input(f"Enter new publication year - {books[book_id]['year']} (leave blank to keep current): ") or books[book_id]['year']
    copies = input(f"Enter new number of copies - {books[book_id]['copies']} (leave blank to keep current): ") or books[book_id]['copies'] 
    books[book_id] = {
        'title': title,
        'author': author,
        'year': year,
        'copies': copies
    }   


    print(f"Book with ID {book_id} updated successfully.\n")

def delete_book():
    book_id = input("Enter the book ID to delete: ")
    
    if book_id not in books:
        print(f"No book found with ID {book_id}.\n")
        return
    
    del books[book_id]
    print(f"Book with ID {book_id} deleted successfully.\n")

def search_book():
    book_id = input("Enter the book ID to search: ")
    
    if book_id in books:
        info = books[book_id]
        print(f"Book found: ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Year: {info['year']}, Copies: {info['copies']}\n")
    else:
        print(f"No book found with ID {book_id}.\n")

def list_books():
    if not books:
        print("No books available.\n")
    else:
        print("List of Books:")
        for book_id, info in books.items():
            print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Year: {info['year']}, Copies: {info['copies']}")


if __name__ == "__main__":
    
    while True:
        if login():
            menu()
        else:
            print("Login failed. Please try again.")
    