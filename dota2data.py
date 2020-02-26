import dota2api
import requests
import pprint
import json
import pandas as pd
import numpy as np
r = requests.get("https://api.opendota.com/api/matches/74170846")

pprint.pprint(json.loads(r.text))

r = requests.get("https://api.opendota.com/api/matches/5258062710")
r = requests.get("https://api.opendota.com/api/players/76561198140336085/recentMatches")



pprint.pprint(json.loads(r.text))


api = dota2api.Initialise("54699EC1DAEC662D994DAADE57148354", raw_mode = True)


api.get_heroes()


api.get_match_details(match_id = 5258276949)

api.get_player_summaries(76561198140336085) 

76561198140336085 - 76561197960265728

api.get_player_summaries(76561198053925328)


from bs4 import BeautifulSoup
import chardet
'''
creat beautifulsoup
'''
def creat_bs(url):
    result = requests.get(url)
    e=chardet.detect(result.content)['encoding']
    #set the code of request object to the webpage's code
    result.encoding=e
    c = result.content
    soup=BeautifulSoup(c,'lxml')
    return soup
'''
build urls group
'''
def build_urls(prefix,suffix):
    urls=[]
    for item in suffix:
        url=prefix+item
        urls.append(url)
    return urls
'''
acquire all the page titles and links and save it
'''
def find_title_link(soup):
    titles=[]
    links=[]
    try:
        contanier=soup.find('div',{'class':'container_padd'})
        ajaxtable=contanier.find('form',{'id':'ajaxtable'})
        page_list=ajaxtable.find_all('li')
        for page in page_list:
            titlelink=page.find('a',{'class':'truetit'})
            if titlelink.text==None:                   
                title=titlelink.find('b').text
            else:
                title=titlelink.text
            if np.random.uniform(0,1)>0.90:
                link=titlelink.get('href')
                titles.append(title)
                links.append(link)
    except:
        print('have none value')
    return titles,links




'''
acquire reply in every topic of 10 page
'''
def find_reply(soup):
    replys=[]
    try:
        details=soup.find('div',{'class':'hp-wrap details'})
        form=details.find('form')
        floors=form.find_all('div',{'class':'floor'})
        for floor in floors:
            table=floor.find('table',{'class':'case'})
            if floor.id!='tpc':
                if table.find('p')!=None:
                    reply=table.find('p').text
                else:
                    reply=table.find('td').text
                replys.append(reply)
            elif floor.id=='tpc':
                continue
    except:
        return None
    return replys



'''
acquire information from hupu pubg bbs
'''
url='https://bbs.hupu.com/pubg'
page_suffix=['','-2','-3','-4','-5','-6','-7','-8','-9','-10','-11','-12',
'-13','-14','-15','-16','-17','-18','-19','-20','-21','-22','-23','-24',
'-25','-26','-27','-28','-29','-30']
urls=build_urls(url,page_suffix)

title_group=[]
link_group=[]
for url in urls:
    soup=creat_bs(url)
    titles,links=find_title_link(soup)
    for title in titles:
        title_group.append(title)
    for link in links:
        link_group.append(link)


reply_urls=build_urls('https://bbs.hupu.com',link_group)
reply_group=[]
for url in reply_urls:
    soup=creat_bs(url)    
    replys=find_reply(soup)
    if replys!=None:
        for reply in replys:
            reply_group.append(reply)




'''
creat wordlist and save as txt
'''
wordlist=str()
for title in title_group:
    wordlist+=title

for reply in reply_group:
    wordlist+=reply

def savetxt(wordlist):
    f=open('wordlist.txt','wb')
    f.write(wordlist.encode('utf8'))
    f.close()    
savetxt(wordlist)