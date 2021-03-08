#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 2. Weekly Challenge 7: OOP Design & Implementation

Challenge 7

You were just given the task to improve the design of the following Python script. 

1.	TAC Engineers are complaining that they have to implement PS methods in their CiscoTacEngineer class. 
2.	Professional Services teams are frustrated about implementing TAC methods in their CiscoPSEngineer class. 
3.	TAC is currently working with R&S, Wireless and Data Center technologies (but there is a rumor that they will need to start working with Security cases also). 
4.	Lastly CX Mexico just realized that there are some Third Party Methods implemented in the Cisco Engineer class, and this has to stop immediately! 

(TIP: use the The First 5 Principles of Object Oriented Design S.O.L.I.D.)

You were asked to document your code explaining the reasons why you made those changes.


"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Luis Arturo Pérez"]
__date__ = "2021/03/07"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"


import abc
from abc import ABCMeta


class CiscoEngineer(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def Work(self):
        pass


class CiscoTacEngineer(CiscoEngineer):
    def __init__(self,name):
        CiscoEngineer.__init__(self, name)
    
    def Work(self):
        print("Hey!, I'm working on a TAC case.")


    def solveCase(self, techStripe):
        if(techStripe=='RS'):
            print("R&S cases are a piece of cake")
        elif(techStripe=='Wireless'):
            print("I love to solve Wireless cases")
        elif(techStripe=='DC'):
            print("DC is my passion")
        elif(techStripe=='Security'):
            print("Security is my passion")



class CiscoPSEngineer(CiscoEngineer):
    def __init__(self,name):
        CiscoEngineer.__init__(self, name)
    
    def Work(self):
        print("Hey!, I'm working on a PS deliverable.")


def main():



if __name__ == "__main__":
    main()