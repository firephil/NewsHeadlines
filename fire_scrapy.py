from joblib import Parallel, delayed
from bs4 import BeautifulSoup as soup
import requests
from typing import List
import os

# use a user agent header to avoid Blocking from web servers
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

class Article:

    def __init__(self, title = None , text = None, link = None, date= None):
        self.title = title
        self.text = text
        self.link = link
        self.date = date

    def __repr__(self):

        return f"<Article Title: {self.title}  Text: {self.text} Link: {self.link} Date: {self.date}>"


def scrape(url) -> soup:
    
    try :
        r = requests.get(url,headers=headers)
        page = soup(r.content, "html.parser")
        return page
    
    except:
        print(f"error {url} not downloaded")
        return soup() # empty soup

def getLinks(page:soup) -> List[str]:

    ls = []
    lines = page.find_all('a')
    
    for line in lines:
        href = line.get('href')
        ls.append(href)
    return ls

def scrapeLocal(path:str) -> soup:
    
    with open(path, 'r') as file:
        page = soup(file, "html.parser")
    
    return page
    
def savePage(page:soup, path: str):
    
    with open(path, 'w') as file:
        file.write(page.prettify())
