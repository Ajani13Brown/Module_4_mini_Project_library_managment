class User():
    def __init__(self, name, address, phone_number, password,):
#may need to remove password if login decide against login function
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.__password = password
        self.books = []

    def user_info(self):
        print(f'Name: {self.name}')
        print(f'address: {self.address}')
        print(f'Phone Number: {self.phone_number}')

    def borrow_book(books, current_user):
        title = input("Enter the title of the book you want to borrow: ").title()
        for book in books:
            if book.title == title:
                if book.available:
                    print(current_user)
                    current_user.books.append(book)
                    book.available = False
                    print(f"{current_user.name} has borrowed '{book.title}'.")
                else:
                    print(f"Sorry, '{book.title}' is not available for borrowing.")

                    
    def add_user(users):
        name = input('Name: ').title()
        address = input('Address: ').title()
        phone = input('Phone: ')
        password = input('password: ')
        new_user = User(name, address, phone, password)    # coppied from Library(main_menu) file may remove
        users.append(new_user)
        print('User Created')
        print('Logging in...')
        current_user = new_user
        print(current_user.user_info())
        return current_user

