#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:13:12 2019

@author: nawal
"""

import csv
import json

teams = []
total_played = []
winner = []
d = {}

# Read csv file 
with open('matches.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        
        # teams name save in teams
        # total played game save in total_played variable
        teams.append(row[4])
        total_played.append(row[4])
        total_played.append(row[5])
        winner.append(row[10])
        
csvFile.close()
teams = set(teams)
teams.remove('team1')

#data save into the dictionary
for team in teams:
    d[team] = {"Total_played": total_played.count(team), "won": winner.count(team), "lost": total_played.count(team)-winner.count(team)}
        
#dictionary converted into the json form
d = json.dumps(d)
print(d)
    