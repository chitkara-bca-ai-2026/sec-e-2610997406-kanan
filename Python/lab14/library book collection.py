books = [
    ("Python Basics", "John", "2019", "Programming"),
    ("AI Guide", "Smith", "2020", "AI"),
    ("Cloud Computing", "David", "2021", "Cloud Computing"),
    ("Robotics", "Alex", "2022", "Robotics")
]

library_categories = set()

for book in books:
    library_categories.add(book[3])

student_wishlist = {
    "AI",
    "Cloud Computing",
    "Robotics",
    "Cybersecurity"
}

while True:
    print("===== LIBRARY MENU =====")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        print("Library Books:")
        for book in books:
            print(book)

    elif choice == "2":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = input("Enter year: ")
        category = input("Enter category: ")

        new_book = (title, author, year, category)
        books.append(new_book)
        library_categories.add(category)

        print("Book added successfully!")

    elif choice == "3":
        print("Library Categories:")
        print(library_categories)

    elif choice == "4":
        category = input("Enter requested category: ")
        student_wishlist.add(category)
        print("Category added to wishlist!")

    elif choice == "5":
        print("Categories in both:")
        print(library_categories & student_wishlist)

        print("Missing Categories:")
        print(student_wishlist - library_categories)

        print("All Categories:")
        print(library_categories | student_wishlist)

    elif choice == "6":
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Enter 1 to 6.")
