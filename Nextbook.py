#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri May 20 14:57:03 2016
@author: Tony
"""

import csv
import random

class Book(object):

    def __init__(self):
        self.csvfile = r'C:\Users\Tony\Desktop\Data sets\Books.csv'
       
    def what_book(self):
        with open(self.csvfile, 'rt') as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader if row['status'] == 'to read'.lower()]
            book_choice = random.chocie(rows)
            suggestion = {k: book_choice[k] for k in book_choice.keys() & {'title', 'author'}}
            
            return suggestion
            
NextBook = Book()

if __name__ == '__main__':
  while True:
    user_input = input("Do you need a book recommendation? Yes or no: ").lower()
    if user_input == 'yes':  
        print(NextBook.what_book())
        
    elif user_input == 'no':
        break
    
    elif user_input == 'end'.lower():
        break

    else:
      print()  
      print("Let's try something else, shall we?")
      print()
      
      
      
      
