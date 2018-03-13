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
        self.csvfile = r'/Users/anthonymandelli/Repos/nextbook/Nextbook/Books.csv'

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

        fields = [nbt1, author1]

        with open(self.csvfile, 'a', newline='') as library:

            writer = csv.writer(library, delimiter=',')

            line_number = Book.book_line(self)

            writer.writerow([line_number] + fields)

            return "Added {}".format(newbook)
