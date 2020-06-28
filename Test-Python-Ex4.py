# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:42:15 2020

@author: Morgann
"""

## Write a Python program to get the number of followers of a specific account on Twitter 
#(taking an url as an input, for example https://twitter.com/KMbappe)

import requests
from bs4 import BeautifulSoup

def scraping_twitter(url) :
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    follower = ""
    ligne = 0
    verif = False
    while(verif == False) :
        for i in soup.findAll('a'):
            if(i['href'] == '/KMbappe/followers'):
                follower = soup.findAll('a')[ligne]['title']
                verif = True
                ligne += 1
    return int(follower.replace("&nbsp;", ""))
    
    
    
    