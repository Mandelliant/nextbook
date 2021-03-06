import sys
import os

from book_class import Book



print()
print('---------------------------------')
print('       NEXTBOOK MAIN MENU        ')
print('---------------------------------')
print()

if __name__ == '__main__':
    while True:

        print ('What would you like to do?')
        print ('1. Add a new book')
        print ('2. Get a reading suggestion')
        menu_choice = input('Choose 1 or 2: ')
        selection = int(menu_choice)


        if selection == 1:

            new_title = Book()

            print("\nAdd a new book to the library:")
            print()

            nbt = input("Title: ").title()
            author = input("Author: ").title()

            print()
            print(new_title.add_book(nbt, author))
            print('\nLibrary updated')
            print()

        elif selection == 2:

            suggestion = Book()
            print()
            print(suggestion.what_book())
            print()

        elif selection == 3:
            break

        else:
            print('\nPlease choose 1 or 2')
            print()
