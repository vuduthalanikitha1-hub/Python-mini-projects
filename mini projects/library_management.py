
books = []

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book name: ")
    author = input("Enter author name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print("Book added successfully!")


def display_books():
    if not books:
        print("No books available.")
        return

    print("\n--- Library Books ---")

    for book in books:
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", book["status"])
        print("-------------------")


def search_book():
    book_id = input("Enter book ID to search: ")

    for book in books:
        if book["id"] == book_id:
            print("Book found:", book["title"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            return

    print("Book not found.")


def issue_book():
    book_id = input("Enter book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")


def return_book():
    book_id = input("Enter book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                print("Book returned successfully!")
            else:
                print("This book was not issued.")
            return

    print("Book not found.")


def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice. Try again.")


main()
