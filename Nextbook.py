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


#stuck on writing to appropriate columns
    def add_book(self):
        #with open(self.csvfile, 'ab', newline='') as library:
        with open(self.csvfile, 'ab') as library:
            writer = csv.writer(library, delimiter=',')
            tcolumn = [column for column in writer if column == 'title'.lower()]

            acolumn = [column for column in writer if column == 'author'.lower()]

            writer.writerows(zip(nbt, author)

            #['X', nbt, author])

            #return NewBook.add_book()

            return "Added {}".format(newbook)


NewBook = Book()

if __name__ == '__main__':
  while True:
    print("\nAdd a new book to the library:")
    print()

    nbt = [input("Title: ").title()]
    author = [input("Author: ").title()]
    newbook = '{} by {}'.format(nbt, author)


    print()
    print(NewBook.add_book())
    #print("Added {}".format(newbook))
    break


NextBook = Book()

if __name__ == '__main__':
  while True:
    user_input = input("\nDo you need a book suggestion? Yes or no: ").lower()
    if user_input == 'yes':
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
