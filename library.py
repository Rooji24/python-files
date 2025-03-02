class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    library = Library(['Python', 'C++', 'Java', 'C', 'C#'], "Central Library")
    while True:
        print(f"Welcome to the {library.name}. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            library.displayBooks()
        elif user_choice == 2:
            library.lendBook(input("Enter your name: "), input("Enter the name of the book: "))
        elif user_choice == 3:
            library.addBook(input("Enter the name of the book: "))
        elif user_choice == 4:
            library.returnBook(input("Enter the name of the book: "))
        else:
            print("Not a valid option")
        print("Press q to quit and c to continue")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                break
            else:
                print("Please enter a valid option")

