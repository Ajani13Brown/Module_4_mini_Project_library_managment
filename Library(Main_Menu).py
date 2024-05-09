import os
from Users_and_functions import User
from Books_and_functions import Book
from Authors_and_functions import Author

users = []
authors = []
books = []



                      #-- User Menu And Fuctions
#------------------------------------------------------------------------------------------------------------------------------------------

def add_user(users):
    name = input('Name: ').title()
    address = input('Address: ').title()
    phone = input('Phone: ')
    password = input('password: ')
    new_user = User(name, address, phone, password)  # Made a copy in user file to see if that would allow me to track current user
    users.append(new_user)                           # Currently using my User.add_user in my library menu, may need to switch back
    print('User Created')
    print('Logging in...')
    current_user = new_user
    print(current_user.user_info())
    return current_user

def search_users(users):
    name = input('Search Name: ').title()
    for user in users:
        if user.name == name:
            print('User Found!')
            user.user_info()
            return User
            
def display_users(users):
    for user in users:
        user.user_info()
        print(User)

def login():
    try:
        option = int(input('''
            Login options
        --------------------
        1. Existing User
        2. New User
        > '''))
    except ValueError:
        print('Please respond only with numbers!')
    else:
        if option == 1:
            username = input("Username: ")
            password = input("Password: ")
            for user in users:
                if user.name == username and user.password == password:
                    global current_user       # when creating my borrow_book function i got an error message stating my Current_user value was none
                    current_user = user       # despite changing it to a user when reseach online how to correct this and i say code that used "global"
                    print("Login successful.") # I asked chatgpt to explain it to me and i appears to be a function that changes a variables from a 
                    return current_user        #local location to a global one this is to ensure that my borrow_book function see my current_user

                else:
                    print("Invalid Username,Try agan")
        elif option == 2:
            add_user(users)
        else:
            print(f'Sorry {option} is not a valid option')
            print(f'Let try that again and please respond with only 1,2, 3 or 4')

def user_options():
    while True:
        try:
            option = int(input(''' 
                User Options:
            -----------------------
                1. Add a new user
                2. View user details
                3. Display all users
                4. Main Menu
                > '''))
        except ValueError:
            print('Please respond only with numbers!')
        else:
            if option == 1:
                current_user = add_user(users)
                return current_user
            elif option == 2:
                search_users(users)
            elif option == 3:
                display_users(users)
            elif option == 4:
                print('returning to main menu')
                break
            else:
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1,2, 3 or 4')



                          #-- Author menu and Functions
#------------------------------------------------------------------------------------------------------------------------------------------


def add_author(authors):
    name = input('Author Name: ')
    new_author = Author(name)
    Author.author_info(new_author)
    authors.append(new_author)

def search_authors(authors):
    name = input('Search Name: ').title()
    for author in authors:
        if author.name == name:
            print('Pulling up Author details')
            author.author_info()
        if name not in authors:
            print(f'{name} not found in authors')

def display_authors(authors):
    for author in authors:
        author.author_info()


def author_options():
    while True:
        try:
            option = int(input(''' 
                Author Options:
            -----------------------
                1. Add a new author
                2. View author details
                3. Display all authors
                4. Main Menu
                > '''))
        except ValueError:
            print('Please respond only with numbers!')

        else:
            if option == 1:
                add_author(authors)
            elif option == 2:
                search_authors(authors)
            elif option == 3:
               display_authors(authors)
            elif option == 4:
                print('Returning to main menu')
                break
            else:
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1,2, 3 or 4')




                            #-- Book menu and fuctions
#----------------------------------------------------------------------------------------------------------------------------------------


def add_book():
    title = input('title: ').title()
    author = input('Author: ').title()     #need to add funtionality to add author to Authors with book in titles when adding a book
    genre = input('Genre: ').title()
    new_book = Book(title, author,genre)
    books.append(new_book)

def display_books(books):
    for book in books:
        if book.available is True:
            book.book_info()

def search_books(books):
    title = input('Search Book: ').title()
    for book in books:
        if book.title == title:
            print('Pulling up book details')
            book.book_info()
        else:
            print(f'{book} not in library inventory')

# def borrow_book(books, current_user):
#     title = input("Enter the title of the book you want to borrow: ").title()
#     for book in books:
#         if book.title == title:
#             if book.available:
#                 current_user.books.append(book)
#                 book.available = False
#                 print(f"{current_user.name} has borrowed '{book.title}'.")
#             else:
#                 print(f"Sorry, '{book.title}' is not available for borrowing.")


def book_options():
    while True:
        try:
            option = int(input(''' 
                book Options:
            -----------------------
                1. Add a new book
                2. Borrow a book
                3. Return a book
                4. Search for a book
                5. Display all books
                6. Main Menu
                > '''))
        except ValueError:
            print('Please respond only with numbers!')

        else:
            if option == 1:
                add_book()
                print(books)
            elif option == 2:
               display_books(books)
               User.borrow_book(books,current_user)
            elif option == 3:
                print('working')
                pass
            elif option == 4:
                search_books(books)
            elif option == 5:
                display_books(books)
            elif option == 6:
                print('returning to main menu')
                break
            else:
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1, 2, 3, 4, 5 or 6')

                                #-- Main Menu/ Command Line Interface
#-----------------------------------------------------------------------------------------------------------------------------------------

def library_menu():
    current_user = None
    os.system('cls')
    print( "Welcome to the Coding Temple Library Management System!")
    print('Lets get you logged in')
    User.add_user(users)
    #login()
    while True:
        try:
            print(current_user)
            option = int(input(''' 
                Main Menu:
            ------------------
            1. Book Options
            2. User Options
            3. Author Options
            4. Exit Library
            > '''))

        except ValueError:
            print('Please respond only with numbers!')

        else:
            if option == 1:
                os.system('cls')
                book_options()
            elif option == 2:
                os.system('cls')
                current_user = user_options()
            elif option == 3:
                os.system('cls')
                author_options()
            elif option == 4:
                os.system('cls')
                print('Exiting library')
                print('Thank you have a nice day')
                break
            else:
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1,2,3 or 4')
            

library_menu()

