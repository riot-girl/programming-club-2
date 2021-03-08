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
__credits__ = ["MXC Programming Club, Luis Arturo Pérez"]
__date__ = "2021/03/07"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"


import datetime
from dateutil import parser

def pull_data():
    all_presidents = []

    with open("presidents.txt") as PRES:
        for rec in PRES:
            # Data sctructure: 
            # President:Last_Name:First_Name:Birth_day:Death_day:Birth_Place:
            # Birth_State:Start_Date:End_Date:Party
            _, last_name, first_name, _, _, _, _, start_date, end_date, _ = rec.split(":")

            start_date = parser.parse(start_date)
            if end_date == 'NONE':
                end_date = datetime.datetime.now()
            else:
                end_date = parser.parse(end_date)
            
            deltatime = end_date - start_date
            full_name = '{} {}'.format(first_name, last_name)

            all_presidents.append((deltatime, full_name))
                
    return all_presidents


def main():
    all_presidents = pull_data()

    for deltatime, name in reversed(sorted(all_presidents)):
        print(name, " presided ", int(deltatime.days/365), 'years', int(deltatime.days%365/30), 'months')

    
if __name__ == "__main__":
    main()