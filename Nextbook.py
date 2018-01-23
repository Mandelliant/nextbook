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


"""
    def add_book(self):
        with open(self.csvfile, 'wt', newline='') as f:
"""
        #Disabled while developing function
        #Return 'added [title] by [author] to the library'



NewBook = Book()

if __name__ == '__main__':
  while True:
    print("Add a new book to the library:")
    print()

    nbt = input("Title: ").title()
    author = input("Author: ").title()
    newbook = '{} by {}'.format(nbt, author)

    print()
    print("Added {}".format(newbook))
    break


NextBook = Book()

if __name__ == '__main__':
  while True:
    user_input = input("Do you need a book suggestion? Yes or no: ").lower()
    if user_input == 'yes':
        print(NextBook.what_book())


    elif user_input == 'end'.lower():
        break

    else:
      print()
      print("Let's try something else, shall we?")
      print()
      break
