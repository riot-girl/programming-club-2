#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 2. Weekly Challenge 4: Complexity Optimization

There is a server that provides certain processes to the entire company. The 
server is experiencing very long throughput issues. Within the server there 
are very important processes that cannot be stopped at any part of the day; 
therefore, you have been assigned two different algorithms that are not 
critical for you to optimize their execution.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Luis Mundo"]
__date__ = "2021/03/07"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"


from datetime import datetime

def getDivisors(num):
    print("The divisors of the number are:")
    for i in range(1,num+1):
        if(num%i==0):
            print(f'{i}',end=' ')

def getDivisorsimp(num):
    print("The divisors of the number are:")
    max = num
    i = 1
    while max >0 and i < max:
        if(num%i==0):
            max = num/i
            print(f'{i} {int(num/i)}',end=' ')
        i += 1

def prime(num):
    # Function to check if a number is prime or not
    start = datetime.now()

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                getDivisors(num);
                break
            else:
                print(num,"is a prime number")
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")
    end = datetime.now()
    print(f'\nTime to run: {end-start}')

def primeimp(num):
    # Function to check if a number is prime or not
    start = datetime.now()

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                getDivisorsimp(num);
                break
            else:
                print(num,"is a prime number")
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")
    end = datetime.now()
    print(f'\nTime to run: {end-start}')

def main():
    num = 35000

    # To take input from the user
    #num = int(input("Enter a number: "))
    
    prime(num)
    primeimp(num)


if __name__ == "__main__":
    main()