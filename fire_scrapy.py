from joblib import Parallel, delayed
from bs4 import BeautifulSoup as soup
import requests
from typing import List
import os
import feedparser
from news import Article

# use a user agent header to avoid Blocking from web servers
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

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

def getRSS(url) ->List[Article]:
    feed = feedparser.parse(url)
   
    ls:List[Article] = []

    for entry in feed.entries:
        article = Article(entry.title, entry.summary,entry.link,entry.published,entry.category)
        ls.append(article)

    return ls


if( __name__ == '__main__'):
   pass