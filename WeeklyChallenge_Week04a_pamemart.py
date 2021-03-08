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

def printArray(arr):
    for i in range(len(arr)):
        print ("%d, " %arr[i], end="")

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
        print (f"\nThis iteration array is:", end=' ')
        printArray(arr)
    
def bubbleSortimp(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(0,n-1):
        sorted = 0
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted += 1
        if i > 0 and sorted == 0:
            break

        print (f"\nThis iteration array is:", end=' ')
        printArray(arr)

def bubbleSortrev(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(0,n-1):
        sorted = 0
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted += 1
        if i > 0 and sorted == 0:
            break

        print (f"\nThis iteration array is:", end=' ')
        printArray(arr)

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]
    start1 = datetime.now()
    print (f" \nFirst Unsorted array is:", end=' ')
    printArray(arr)

    bubbleSort(arr)

    print (f" \nFinal First Sorted array is:", end=' ')
    printArray(arr)
    end1 = datetime.now()
    print("\nTime 1:    " + str(end1-start1))

    arr = [64, 34, 25, 12, 22, 11, 90]
    start2 = datetime.now()
    print (f" \nSecond Unsorted array is:", end=' ')
    printArray(arr)
    bubbleSortimp(arr)

    print (f" \nFinal Second Sorted array is:", end=' ')
    printArray(arr)
    end2 = datetime.now()
    print("\nTime 2:    " + str(end2-start2))

    arr = [64, 34, 25, 12, 22, 11, 90]
    start2 = datetime.now()
    print (f" \nThird Unsorted array is:", end=' ')
    printArray(arr)
    bubbleSortrev(arr)

    print (f" \nFinal Third Sorted array is:", end=' ')
    printArray(arr)
    end2 = datetime.now()
    print("\nTime 3:    " + str(end2-start2))

if __name__ == "__main__":
    main()