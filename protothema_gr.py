from fire_scrapy import Article
import feeder
from typing import List
import pickle

URL = "https://www.protothema.gr/rss"

def get()->List[Article]:
    return feeder.getRSS(URL)

def saveToFile():
    feeder.save(URL,get())

if( __name__ == '__main__'):
    saveToFile()