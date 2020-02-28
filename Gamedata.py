from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from time import sleep
from random import randint
# csv file name 
filename = "Dota_buff.csv"
api = dota2api.Initialise("54699EC1DAEC662D994DAADE57148354", raw_mode = True)
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    #fields = csvreader.next() 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  

def get_match(match_id):
    match = pd.DataFrame()
    try:
        match = api.get_match_details(match_id)
    except:
        pass
    return match


def get_history(id):
    match_hist = pd.DataFrame()
    try:
        match_hist = api.get_match_history(id)
    except:
        pass
    return match_hist

url = 'https://steamcommunity.com/app/570/discussions/'

matches = pd.DataFrame()
history = pd.DataFrame()


Id = pd.DataFrame(rows)[1]
Id = Id.to_list()
Id = Id[1:]
for item in Id:
    history = history.append(pd.DataFrame(get_history(item)))


# Player history file
history.to_csv("player_history.csv")
match_id =[x.get('match_id',0) for x in history['matches']]

for i in match_id:
    matches = matches.append(get_match(i), ignore_index = True)


matches.to_csv("match_details.csv")

player_details = pd.DataFrame()
for i in range(10):
    player_details = player_details.append(pd.DataFrame(matches.players.to_list())[i].apply(pd.Series))


player_details.to_csv("player_match_details.csv")

# get_history(Id[1])
# pd.DataFrame(api.get_match_history(76561198140336085))




# !pip install -U dota2
# import dota2
# dota.request_match_details(match_id)

