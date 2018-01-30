#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Updated Nextbook
@author: Anthony
1/2018
"""

import csv
import random

class Book(object):

    def __init__(self):
        self.csvfile = r'/Users/anthonymandelli/Repos/nextbook/Books.csv'

    def what_book(self):
        with open(self.csvfile, 'rt') as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader if row['status'] == 'to read'.lower()]
            book_choice = random.choice(rows)
            suggestion = {k: book_choice[k] for k in book_choice.keys() & {'title', 'author'}}

            return '{title} by {author}'.format(**suggestion)

    def book_line(self):

        with open(self.csvfile, 'r', newline='') as library:

            line_number = len(library.readlines())

            new_book_id = int(line_number)

            return new_book_id

    def add_book(self, nbt1, author1):

        fields =[nbt1,author1]

        with open(self.csvfile, 'a', newline='') as library:

            writer = csv.writer(library, delimiter=',')

            line_number = Book.book_line(self)

            writer.writerow([line_number] + fields)

            return "Added {}".format(newbook)


NewBook = Book()

if __name__ == '__main__':
  while True:
    print("\nAdd a new book to the library:")
    print()

    nbt = input("Title: ").title()
    author = input("Author: ").title()
    newbook = '{} by {}'.format(nbt, author)


    print()
    print(NewBook.add_book(nbt, author))
    #print("Added {}".format(newbook))
    break

NextBook = Book()

if __name__ == '__main__':
  while True:
    user_input = input("\nDo you need a book suggestion? Yes or no: ").lower()
    if user_input == 'yes':
        print()
        print(NextBook.what_book())


    elif user_input == 'end'.lower():
        break

    else:
      print()
      print("Let's try something else, shall we?")
      print()
      break
      #Return to menu


#changed file path
#fixed \n formatting
