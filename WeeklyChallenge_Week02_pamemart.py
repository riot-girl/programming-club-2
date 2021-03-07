#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 2. Weekly Challenge 2: Recursive Fuctions

You were just given the task of discovering the devices of a mysterious 
network topology, and the connections between them.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Alfonso Sandoval"]
__date__ = "2021/03/07"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

from NETWORK import network

def find_neighbors(seed, file):
    for neighbor in network[seed]:
        file.write(f'{seed} >> {neighbor}\n')
    for neighbor in network[seed]:
        find_neighbors(neighbor,file)        

def main():
    file = open('inventory.txt', 'a')
    seed = 'RA'
    file.write(f'{seed}\n')
    find_neighbors(seed, file)
    file.close()
    
if __name__ == "__main__":
    main()