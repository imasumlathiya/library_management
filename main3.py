# Library Management System

books = []

# FUNCTION TO ADD BOOKS 

def add_book():
    book_id = input("Enter book id: ")
    book_name = input("Enter book name: ")
    author = input("Enter author name: ")

    new_book = {
        "id": book_id,
        "name": book_name,
        "author": author,
        "status": "Available"
    }

    books.append(new_book)
    print("BOOK ADDED SUCCESSFULLY!")

# FUNCTION TO DISPLAY BOOKS
def display_books():
    if len(books) == 0:
        print("NO BOOKS ARE AVAILABLE !!")
        return

    print("\n******** BOOKS IN LIBRARY ********")

    for book in books:
        print("Book ID:", book["id"])
        print("Book Name:", book["name"])
        print("Author:", book["author"])
        print("Status:", book["status"])
        print("**************************")


# FUNCTION TO SEARCH BOOK

def search_book():
    book_id = input("Enter book id: ")

    for book in books:
        if book["id"] == book_id:
            print("\nBook found!")
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            return

    print("BOOK NOT FOUND !!")

# FUNCTION TO ISSUE BOOK

def issue_book():
    book_id = input("Enter book id: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Available":
                book["status"] = "Issued"
                print("BOOK ISSUED SUCCESSFULLY !")
            else:
                print("THIS BOOK IS ALREADY ISSUED !!")

            return

    print("BOOK NOT FOUND !!")

# FUNCTION TO RETURN BOOK

def return_book():
    book_id = input("Enter book id: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Issued":
                book["status"] = "Available"
                print("Book returned successfully!")
            else:
                print("THIS BOOK IS ALREADY AVAILABLE !!")

            return

    print("BOOK NOT FOUND !!")

# FUNCTION TO SAVE BOOKS

def save_books():
    file = open("library.txt", "w")

    for book in books:
        file.write(
            book["id"] + "," +
            book["name"] + "," +
            book["author"] + "," +
            book["status"] + "\n"
        )

    file.close()


# FUNCTION TO LOAD BOOKS

def load_books():
    try:
        file = open("library.txt", "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                book = {
                    "id": data[0],
                    "name": data[1],
                    "author": data[2],
                    "status": data[3]
                }

                books.append(book)

        file.close()

    except FileNotFoundError:
        pass


# Load old books when program starts
load_books()


while True:

    print("\n******** LIBRARY MANAGEMENT SYSTEM ********")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book() # FUNCTION IS BEING CALLED HERE WHICH WAS CREATED EARLIER

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        save_books()
        print("Thank you for using the Library Management System!")
        break

    else:
        print("PLEASE ENTER VALID CHOICE !!")



