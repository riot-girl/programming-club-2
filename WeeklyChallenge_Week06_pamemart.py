#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 2. Weekly Challenge 6: OOP Inheritance, Polymorphism and Interfaces

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Miguel Gutiérrez"]
__date__ = "2021/03/07"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"


import abc
from abc import ABCMeta, abstractmethod
from sys import modules

class Device():

    #Shared Attributes
    def __init__(self, device_name, ip_address, password):
        self.device_name = device_name
        self.ip_address = ip_address
        self.password = password
        self.connect_to()
    
    #Abstract Methods
    @abstractmethod
    def connect_to(self):
        pass


class SSHDevice(Device):

    def connect_to(self):
        print('SSH Connection')
        print('To Device: {}' .format(self.ip_address))
        print('With IP: {}\n\n' .format(self.device_name))


class TelnetDevice(Device):

    def connect_to(self):
        print('Telnet Connection')
        print('To Device: {}' .format(self.ip_address))
        print('With IP: {}\n\n' .format(self.device_name))


def main():
    device_1 = SSHDevice('ASR900', '1.1.1.1', 'cisco')
    device_2 = TelnetDevice('ASR900', '2.2.2.2', 'cisco')

if __name__ == "__main__":
    main()