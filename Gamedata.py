from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from time import sleep
from random import randint


url = 'https://steamcommunity.com/app/570/discussions/'

 

Link = []
Id = []


ourUrl=urllib.request.urlopen(url).read().decode("utf-8")
    
soup=BeautifulSoup(ourUrl,'html.parser')
    #print(soup.prettify())
    
    #all_info=soup.find_all('div',{'class':"responsive_page_content"})
    #print(all_info)
    
    #for i in range(1,len(all_info)):
for item in  soup.find_all('a',{'class':'forum_topic_overlay'}):
    link = item.get('href')
        #print(href)
    Link.append(link)
Link

for i in range(len(Link)):
    Id.append(Link[i].rsplit('/')[-2])
Id


matches = pd.DataFrame()
history = pd.DataFrame()
match_id = [5264233901,5263347490]
for i in match_id:
    print(i)
    matches = matches.append(get_match(i))
api = dota2api.Initialise("54699EC1DAEC662D994DAADE57148354", raw_mode = True)
pd.DataFrame(api.get_match_details(match_id)['players'])

def get_match(match_id):
    return pd.DataFrame(api.get_match_details(match_id))


# 76561198140336085 - 76561197960265728

def get_history(id):
    match_hist = pd.DataFrame()
    try:
        match_hist = api.get_match_history(id)
    except:
        pass
    return match_hist

for item in Id:
    history = history.append(pd.DataFrame(get_history(item)))
get_history(Id[1])
pd.DataFrame(api.get_match_history(76561198140336085))


r = requests.get("https://api.opendota.com/api/players/76561198140336085/recentMatches")



pprint.pprint(json.loads(r.text))




url = "https://api.opendota.com/api/matches/" + str(match_id)
requests.get(url)

json.loads(requests.get(url).text)


!pip install -U dota2
import dota2
dota.request_match_details(match_id)


class(matches)