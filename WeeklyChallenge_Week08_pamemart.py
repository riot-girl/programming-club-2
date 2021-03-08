#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 2. Weekly Challenge 8: Encoding Methods

You work as a programmer for a prestigious Book Store. Your manager gave you 
the task of create an application that takes a DB file that contains the list 
of the most prestigious books available in store.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Manuel Santos"]
__date__ = "2021/03/07"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

from os import system
import time
import xmltodict
import json
import oyaml

db = ['booksdb.xml', 'booksdb.json', 'booksdb.yaml']

def check_menu1(option):
    try:
        # Convert option into number
        val = int(option)
        if val < 1 or val > 4:
            print(f"{option} is not a valid number.\n")
            time.sleep(1)
            return ValueError
        else:
            return val
    except ValueError:
        print(f"{option} is not a valid number.\n")
        time.sleep(1)
        return ValueError

def check_menu2(option):
    try:
        # Convert option into number
        val = int(option)
        if val < 1 or val > 8:
            print(f"{option} is not a valid number.\n")
            time.sleep(1)
            return ValueError
        else:
            return val
    except ValueError:
        print(f"{option} is not a valid number.\n")
        time.sleep(1)
        return ValueError
        
def menu1():
    option = ValueError
    while (option == ValueError):
        system('clear')
        print ("=========================")
        print ("PRESTIGIOUS BOOK STORE")
        print ("=========================")
        print("Select your preferred database:")
        print("1. booksdb.xml")
        print("2. booksdb.json")
        print("3. booksdb.yaml")
        print("4. Exit")
    
        option = input(f"\nEnter an option: ")
        option = check_menu1(option)
    return option

def menu2(dbtype):
    option = ValueError
    while (option == ValueError):
        system('clear')
        print ("==================================")
        print (f"MR. BOOKS DATABASE: {db[dbtype]}")
        print ("==================================")
        print("1. Search books per Title")
        print("2. Search books per Author")
        print("3. Search books per Language")
        print("4. Search books per Published Year")
        print("5. Search small books (< 300 pages)")
        print("6. Search medium books (300-600 pages)")
        print("7. Search large books (> 600 pages)")
        print("8. Exit")
    
        option = input(f"\nEnter an option: ")
        option = check_menu2(option)
    return option

def search_xml(option2, dict):
    if option2 == 1:
        title = input("Enter the Title you want to retrieve: ")
        for book in dict['books']['book']:
            if book['title'] == title:
                print(json.dumps(book, indent=4))
    if option2 == 2:
        author = input("Enter the Author you want to retrieve: ")
        for book in dict['books']['book']:
            if book['author'] == author:
                print(json.dumps(book, indent=4))
    if option2 == 3:
        language = input("Enter the Language you want to retrieve: ")
        for book in dict['books']['book']:
            if book['language'] == language:
                print(json.dumps(book, indent=4))
    if option2 == 4:
        year = input("Enter the Published Year you want to retrieve: ")
        for book in dict['books']['book']:
            if int(book['year']) == int(year):
                print(json.dumps(book, indent=4))
    if option2 == 5:
        for book in dict['books']['book']:
            if int(book['pages']) < 300:
                print(json.dumps(book, indent=4))
    if option2 == 6:
        for book in dict['books']['book']:
            if int(book['pages']) >= 300 and int(book['pages']) <= 600:
                print(json.dumps(book, indent=4))
    if option2 == 7:
        for book in dict['books']['book']:
            if int(book['pages']) > 600:
                print(json.dumps(book, indent=4))

def search_json_yaml(option2, dict):
    if option2 == 1:
        title = input("Enter the Title you want to retrieve: ")
        for book in dict:
            if book['title'] == title:
                print(json.dumps(book, indent=4))
    if option2 == 2:
        author = input("Enter the Author you want to retrieve: ")
        for book in dict:
            if book['author'] == author:
                print(json.dumps(book, indent=4))
    if option2 == 3:
        language = input("Enter the Language you want to retrieve: ")
        for book in dict:
            if book['language'] == language:
                print(json.dumps(book, indent=4))
    if option2 == 4:
        year = input("Enter the Published Year you want to retrieve: ")
        for book in dict:
            if int(book['year']) == int(year):
                print(json.dumps(book, indent=4))
    if option2 == 5:
        for book in dict:
            if int(book['pages']) < 300:
                print(json.dumps(book, indent=4))
    if option2 == 6:
        for book in dict:
            if int(book[5]) >= 300 and int(book['pages']) <= 600:
                print(json.dumps(book, indent=4))
    if option2 == 7:
        for book in dict:
            if int(book['pages']) > 600:
                print(json.dumps(book, indent=4))

def main():
    option1 = menu1()
    if option1 == 1:
        with open('booksdb.xml','r') as xml_file:
            xml_string = xml_file.read()    
        dict = xmltodict.parse(xml_string)
        option2 = menu2(option1-1)
        search_xml(option2, dict)

    if option1 == 2:
        with open('booksdb.json','r') as json_file:
            dict = json.loads(json_file.read())    
        option2 = menu2(option1-1)
        search_json_yaml(option2, dict)

    if option1 == 3:
        with open('booksdb.yaml','r') as yaml_file:
            yaml_string = yaml_file.read()    
            dict = oyaml.load(yaml_string, Loader=oyaml.FullLoader)
        option2 = menu2(option1-1)
        search_json_yaml(option2, dict)
    
if __name__ == "__main__":
    main()