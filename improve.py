#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:18:39 2019

@author: nawal
"""

import csv
teams = []
total_played = []
winner = []
d = {}

# Read csv file 
def loop(data):
    for row in data:
        if data == reader:
            teams.append(row[4])
            total_played.append(row[4])
            total_played.append(row[5])
            winner.append(row[10])
        else:
            d[row] = {"Total_played": total_played.count(row), "won": winner.count(row), "lost": total_played.count(row)-winner.count(row)}
        
with open('matches.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    loop(reader)
        
csvFile.close()

loop(teams)
d.pop('team1')
print(d)
